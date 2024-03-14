![Youtube to M3U](https://i.imgur.com/pCZ5vcS.jpg "YouTube to M3U")

# YouTube Live Link to M3U Bot

This project provides a Telegram bot that extracts the M3U link from a YouTube Live link, enabling users to play live streams in external players such as VLC or include them in IPTV files.

## Features

- Extract M3U links from YouTube Live URLs.
- Easy to use with Telegram.
- Automatic retries for reliable link fetching.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- `pip` for installing dependencies.

## Installation

To install the bot, follow these steps:

- **make sure to include your Telwgram Bot Token in the settings.ini file.**

1. Clone the repository:
   ```bash
   git clone https://github.com/fairy-root/youtube-to-m3u
   ```
2. Navigate to the cloned directory:
   ```bash
   cd youtube-to-m3u
   ```
3. Install the required Python packages:
   ```bash
   pip install pyTelegramBotAPI requests
   ```

## Configuration

1. Rename `settings.ini.example` to `settings.ini`.
2. Open `settings.ini` and replace `Telegram_Bot_Token` with your actual Telegram Bot Token obtained from BotFather.

## Usage

To start the bot, run the following command in your terminal:

```bash
python main.py
```

Once the bot is running, send it a live YouTube link via Telegram, and it will reply with the extracted M3U link.

## Donation

Your support is appreciated:

- USDt (TRC20): `TGCVbSSJbwL5nyXqMuKY839LJ5q5ygn2uS`
- BTC: `13GS1ixn2uQAmFQkte6qA5p1MQtMXre6MT`
- ETH (ERC20): `0xdbc7a7dafbb333773a5866ccf7a74da15ee654cc`
- LTC: `Ldb6SDxUMEdYQQfRhSA3zi4dCUtfUdsPou`


## Contributing

If you have suggestions or improvements, please fork the repository and create a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, please contact @FairyRoot on Telegram.