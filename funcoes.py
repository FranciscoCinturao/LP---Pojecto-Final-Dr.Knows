from chatBot import Chatbot

def resposta():
    #capturar a resposta do Usario e  a processar
    resp = input('>: ')
    resp = resp. lower()
    resp = resp.replace('é','e')
    return resp


def pegaNome(nome):
    if 'o meu nome e ' in nome:
        nome = nome [13:]

    nome = nome.title()
    return nome

def respondeNome(nome):
    conhecidos =['Danilson','Adelxandre']

    if nome in conhecidos:
        frase = 'Olá '
    else:
        frase = 'Muito prazer'
        return frase +nome
