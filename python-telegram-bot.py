import telegram
import os
import time
import argparse
import random


chat_id = "@download_bott"
bot = telegram.Bot(token='7145461467:AAG2NGgXg19dbyzC1w2jUe1yDkEIZkpt5T8')


bot.send_message(chat_id=chat_id, text="hello")

def send_files(delay):
    while True:
        tree = os.walk('images')
        for folder_contents in tree:
            dirpath, dirnames, filenames = folder_contents
            random.shuffle(filenames)
            for image in filenames:
                with open(f"images/{image}", 'rb') as my_file:
                    bot.send_document(chat_id=chat_id, document=my_file)
                time.sleep(5)
            time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(description='бот присылает фото космоса')
    parser.add_argument('--delay', help='выберете задержку', default=14400)
    args = parser.parse_args()
    send_files(args.delay)


if __name__ == "__main__":
    main()