import configparser
import telebot
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests
import re

# Load settings from ini file
config = configparser.ConfigParser()
config.read('settings.ini')
TOKEN = config.get('Settings', 'TOKEN')
TIMEOUT = config.getint('Settings', 'TIMEOUT', fallback=15)
RETRIES = config.getint('Settings', 'RETRIES', fallback=5)
BACKOFF_FACTOR = config.getfloat('Settings', 'BACKOFF_FACTOR', fallback=0.1)

bot = telebot.TeleBot(TOKEN)

def setup_session() -> requests.Session:
    session = requests.Session()
    retries = Retry(total=RETRIES, backoff_factor=BACKOFF_FACTOR, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    return session

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send me a Live YouTube link, and I'll try to find the .m3u8 link for you!")
    
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "This bot is created to help users fetch .m3u8 links from Live YouTube URLs. For any questions or suggestions, please contact @FairyRoot. Enjoy!")

@bot.message_handler(func=lambda message: True)
def grab(message):
    url = message.text
    if not ("youtube.com" in url or "youtu.be" in url):
        bot.reply_to(message, "Please provide a valid YouTube URL.")
        return
    
    session = setup_session()
    try:
        response = session.get(url, timeout=TIMEOUT).text
        if '.m3u8' in response:
            end = response.find('.m3u8') + 5
            tuner = 100
            while True:
                if 'https://' in response[end-tuner:end]:
                    link = response[end-tuner:end]
                    start = link.find('https://')
                    end = link.find('.m3u8') + 5
                    bot.reply_to(message, link[start:end])
                    break
                else:
                    tuner += 5
        else:
            bot.reply_to(message, "M3U link not found in response. Try sending a Live YouTube link.")
    except requests.exceptions.RequestException:
        bot.reply_to(message, "Failed to fetch the page. Please try again later.")
    except Exception as e:
        bot.reply_to(message, f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    print("[ * ] Bot is running...")
    bot.polling()