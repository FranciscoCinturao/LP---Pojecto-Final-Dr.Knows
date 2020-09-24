import telepot
from time import sleep
from chatBot import Chatbot

telegram = telepot.Bot("1121265970:AAG8BXZRuvTJeymhoj4adQQ4tv3SXefuiwc")
bot = Chatbot('Kelly')


def receberMsg(msg):
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase, telegram, chatID, msg)
    if isinstance(resp, str):
        bot.fala(resp)
        telegram.sendMessage(chatID, resp)
    else:
        if resp != None:
            bot.fala(resp['mess'])
            #chatID = msg['chat']['id']
            telegram.sendMessage(
                chatID, resp['mess'], reply_markup=resp['reply_markup'])  # name of test


telegram.message_loop(receberMsg)

while True:
    sleep(60)

    message_loop
