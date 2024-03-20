import telegram


chat_id = "@download_bott"
bot = telegram.Bot(token='7145461467:AAG2NGgXg19dbyzC1w2jUe1yDkEIZkpt5T8')

bot.send_message(chat_id=chat_id, text="hello")
bot.send_document(chat_id=chat_id, document=open("images\spaceX_0.jpeg", 'rb'))