from chatBot import Chatbot
Bot = Chatbot ('Kelly')

Bot.fala("Hi! My name is Kelly.")
frase = Bot.escuta()
Bot.fala(Bot.pensa(frase))
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if resp == 'tchau':
        break
