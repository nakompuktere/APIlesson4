import telegram
import os
import time
import argparse
import random
from dotenv import load_dotenv


def send_files(delay, chat_id, bot):
    while True:
        tree = os.walk('images')
        for folder_contents in tree:
            dirpath, dirnames, filenames = folder_contents
            random.shuffle(filenames)
            for image in filenames:
                with open(f"images/{image}", 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(5)
            time.sleep(delay)

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))
    default_chat_id = os.getenv("TG_CHAT_ID")
    parser = argparse.ArgumentParser(description='бот присылает фото космоса')
    parser.add_argument('--chat_id', help='ваш chat id', default=default_chat_id)
    parser.add_argument('--delay', help='выберете задержку', default=14400, type=int)
    args = parser.parse_args()
    send_files(args.delay, args.chat_id, bot)


if __name__ == "__main__":
    main()