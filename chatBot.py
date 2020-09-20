import json
import time
import subprocess as s
# import wikipedia
from words import words
start = 0
ready = 0
answers = {}
start_time = None


class Chatbot():

    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            with open(nome+'.json', 'w') as memoria:
                memoria.write(
                    '[["Danilson","Adelxandre"],{"hi": "Hello, what is your name?","bye":"Bye bye!"}]')
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None, nome]
        self.lastMess = ""
        # print(historico)
        self.disciplina = ""

    def escuta(self, frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        if 'execute ' in frase:
            return frase
        frase = frase.lower()
        return frase

    def write_to_db(self, id, lang):
        with open('db.json', 'r') as jfr:
            jf_file = json.load(jfr)
        with open('db.json', 'w') as jf:
            jf_target = jf_file[0]['users']
            user_info = {id: {'uid': id, 'lang': lang}}
            jf_target.append(user_info)
            json.dump(jf_file, jf, indent=4)

    def check_userid_db(self, uid):
        with open('db.json', 'r') as jfr:
            jf_file = json.load(jfr)
            item = jf_file[0]['users']
            for y in range(len(item)):
                for key in item[y].keys():
                    if int(key) == int(uid):
                        return True

    def get_lang_userid_db(self, uid):
        with open('db.json', 'r') as jfr:
            jf_file = json.load(jfr)
            item = jf_file[0]['users']
            for y in range(len(item)):
                for key in item[y].keys():
                    if int(key) == int(uid):
                        return item[y][key]["lang"]

    def set_lang_db(self, uid, lang):
        with open('db.json', 'r') as jfr:
            jf_file = json.load(jfr)
        with open('db.json', 'w') as jf:
            item = jf_file[0]['users']
            for y in range(len(item)):
                for key in item[y].keys():
                    if int(key) == int(uid):
                        item[y][key]["lang"] = lang
                        json.dump(jf_file, jf, indent=4)
                        return True

    def pensa(self, frase, telegramm, chatID, tipoMsg):

        global answers
        global ready
        global start
        global start_time

        if frase == '/test':
            print(words[self.get_lang_userid_db(
                tipoMsg['from']['id'])]["lis3"])
        if frase == 'selecione linguagem' or frase =='/selectlanguage' or frase == 'language selection':
            if self.check_userid_db(tipoMsg['from']['id']):
                return {"mess": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["selectlang"], "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["main"]}
            else:
                return {"mess": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["no_user"], "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["main"]}
        if frase == 'english':
            if self.check_userid_db(tipoMsg['from']['id']):
                self.set_lang_db(tipoMsg['from']['id'], "EU")
                return {"mess": "Congratulations, you have selected English,"+"\n"+" to change it, write '/selectlanguage'", "reply_markup": words["EU"]["KB"]["dubble"]}
            else:
                return {"mess": "Not that kind of user", "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["main"]}
        if frase == 'portugu\u00EAs':
            if self.check_userid_db(tipoMsg['from']['id']):
                self.set_lang_db(tipoMsg['from']['id'], "PT")
                return {"mess": "Parabéns, você escolheu o idioma português, para alterá-lo escreva '/selectlang'", "reply_markup": words["PT"]["KB"]["dubble"]}
            else:
                return {"mess": "O usuário não existe", "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["main"]}
        if frase == '/start':
            if self.check_userid_db(tipoMsg['from']['id']):
                return {"mess": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["main_start"], "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["dubble"]}
            else:
                self.write_to_db(tipoMsg['from']['id'], "PT")
                return {"mess": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["welcome"], "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["main"]}
        if frase == '/stop':
            start = 0
            return {"mess": "Obrigado por participares nas minhas actividades!!", "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["dubble"]}

        if frase == "selecione disciplina":
            return {"mess": "Escolha a disciplina a que deseja tirar dúvidas.", "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["selecione disciplina"]}
        if frase in ["mbd", "abd"]:
            self.disciplina = frase
            return {"mess": f"Posso esclarecer dúvidas sobre:\n{words[self.get_lang_userid_db(tipoMsg['from']['id'])][self.disciplina]}", "reply_markup": {}}
        if frase == "subject selection":
            return {"mess": "Choose the subject you want to learn about.", "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["select subject"]}
        if frase in ["mdb", "adb"]:
            self.disciplina = frase
            return {"mess": f"I can clarify questions about:\n{words[self.get_lang_userid_db(tipoMsg['from']['id'])][self.disciplina]}", "reply_markup": {}}
        if frase == "quiz":
            answers = {}
            start = 0
            telegramm.sendMessage(chatID, words[self.get_lang_userid_db(tipoMsg['from']['id'])]["quiz_wel"],
                                  reply_markup=words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["k"])  # name of test

        if frase in ['tentar de novo', 'try again']:
            start = 0
            answers = {}
            return {"mess": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["quiz_wel"],
                    "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["k"]}
        if frase == 'começar quiz' or frase == 'start quiz':
            if tipoMsg['from']['id'] not in answers:
                answers[tipoMsg['from']['id']] = []
            else:
                return words[self.get_lang_userid_db(tipoMsg['from']['id'])]["notyou"]
            if len(answers) != telegramm.getChatMembersCount(chatID) - 1:
                return words[self.get_lang_userid_db(tipoMsg['from']['id'])]["waiting4all"]
            else:
                start = 1
                start_time = time.time()
                print(answers)

        # number of questions-1
        question_number = len(
            words[self.get_lang_userid_db(tipoMsg['from']['id'])]["lis1"])
        if start and start <= question_number:
            if frase not in ['começar quiz', 'tentar de novo', 'start quiz', 'try again']:
                if len(answers[tipoMsg['from']['id']]) < start:
                    answers[tipoMsg['from']['id']].append(frase)
            if start != 0:
                for user in answers:
                    if len(answers[user]) != start:
                        telegramm.sendMessage(chatID, words[self.get_lang_userid_db(
                            tipoMsg['from']['id'])]["lis1"][start], reply_markup=words[self.get_lang_userid_db(tipoMsg['from']['id'])]["lis2"][start])
                        break
                else:
                    start = start+1
                    if start <= question_number - 1:
                        telegramm.sendMessage(chatID, words[self.get_lang_userid_db(
                            tipoMsg['from']['id'])]["lis1"][start], reply_markup=words[self.get_lang_userid_db(tipoMsg['from']['id'])]["lis2"][start])
                    else:
                        end_time = time.time()
                        timer = int(end_time-start_time)
                        start = 0
                        reply = ""
                        for user in answers:
                            corretas = 0
                            print(answers[user])
                            print(words[self.get_lang_userid_db(
                                tipoMsg['from']['id'])]["lis3"])
                            for (answer, correct) in zip(answers[user], words[self.get_lang_userid_db(tipoMsg['from']['id'])]["lis3"]):
                                if answer == correct.lower():
                                    corretas += 1

                            timerer = timer
                            if timer >= 70:
                                final_score = corretas*5
                            else:
                                if timer < 30:
                                    timer = 30
                                final_score = corretas*(70-timer)/4
                            if final_score > 100:
                                final_score = 100

                            reply += str(telegramm.getChatMember(chatID, user)["user"]["first_name"])+":"+"\n\n"+words[self.get_lang_userid_db(tipoMsg['from']['id'])]["time"]+str(int(timerer)) + words[self.get_lang_userid_db(tipoMsg['from']['id'])]["sec"] + "\n" + words[self.get_lang_userid_db(
                                tipoMsg['from']['id'])]["truerec"]+str(corretas)+'/10 \n' + words[self.get_lang_userid_db(tipoMsg['from']['id'])]["finalprog"] + str(int(final_score))+'/100\n\n'
                        return {"mess": reply, "reply_markup": words[self.get_lang_userid_db(tipoMsg['from']['id'])]["KB"]["k1"]}

        if frase == 'learn1234':
            return 'Tell the question: '

        # Responde frases que dependem do historico
        ultimaFrase = self.historico[-1]

        print('hist: ', self.historico)

        if ultimaFrase == 'Hello, what is your name?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Tell the question: ':
            self.newquestion = frase
            return 'Tell the question type: '
        if ultimaFrase == 'Tell the question type: ':
            self.newquestiontype = frase
            return 'Tell the answer: '
        if ultimaFrase == 'Tell the answer: ':
            resp = frase

            inserida = False

            for questao in self.frases:
                if self.newquestion in questao['pergunta']:
                    questao['resposta'][self.newquestiontype] = resp
                    inserida = True

            if not inserida:
                self.frases.append({'pergunta': [self.newquestion], 'resposta': {
                                   self.newquestiontype: resp}})

            # self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Got it!'
        if 'Nice to meet you ' in self.historico[-1]:
            return "Please what's the subject you want to learn?"
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass

        if "bye" in frase:
            return "tchau"

        apagar = ["what is",
                  "what is a ", "?", ",", "!", "o que \u00E9 ", "o que \u00E9 a ", "o que \u00E9 uma ", "o que \u00E9 um ", "o que s\u00e3o",
                  "quais os tipos de ", "quais ", "qual ", " a ", "qual a ", "quais s\u00e3o os ",
                  "quais s\u00e3o as ", "como \u00E9 feito o ", "what is a ", "what's a ", "what is ",
                  "what are ", "what is the best place to ", "what are the ", "what are the levels of ",
                  "what kind of ", "what are the ", "what types of ", "exists", "how is it ", "gostaria de saber ", "podes ensinar ",
                  "may i learn about ", "can you teach me ", "dr.knows," "doctor knows"]

        termo = frase
        for a in apagar:
            termo = termo.lower().replace(a, "").strip()

        print(">> ", termo)
        if frase == 'video':
            try:
                return self.lastMess[frase]
            except:
                pass
        if (frase == 'text') or (frase == 'texto'):
            try:
                return self.lastMess[frase]
            except:
                pass
        if frase == 'link':
            try:
                return self.lastMess[frase]
            except:
                pass
        for questao in self.frases:
            if termo in questao['pergunta']:

                if len(questao['resposta']) == 1:
                    for resposta in questao['resposta']:
                        return questao['resposta'][resposta]
                else:

                    telegramm.sendMessage(
                        chatID, words[self.get_lang_userid_db(tipoMsg['from']['id'])]["typq"])
                    separador = ""
                    t = ""
                    for tipo in questao['resposta']:
                        t = t + separador + " " + tipo
                        # print(separador, tipo, end='')
                        separador = words[self.get_lang_userid_db(
                            tipoMsg['from']['id'])]["or"]
                    telegramm.sendMessage(chatID, t)

                    self.lastMess = questao['resposta']
                    return words[self.get_lang_userid_db(tipoMsg['from']['id'])]["respo"]
                    # tipo = input("Qual a resposta que pretende? ")
                    # telegramm.register_next_step_handler(message, func)
                    # return questao['resposta'][tipo]
        if start <= 0 and frase != "quiz":
            if self.check_userid_db(tipoMsg['from']['id'], "EU"):
                return words[self.get_lang_userid_db(tipoMsg['from']['id'])]["understand"]
            else:
                self.write_to_db(tipoMsg['from']['id'], "PT")
                return words[self.get_lang_userid_db(tipoMsg['from']['id'])]["understand"]

    def pegaNome(self, nome):
        if 'my name is ' in nome:
            nome = nome[15:]  # nome.split()[0]

        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Hello '
        else:
            frase = 'Nice to meet you '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome

    def gravaMemoria(self):
        memoria = open(self.nome+'.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):
        if 'execute ' in frase:
            comando = frase.replace('execute ', '')
            try:
                s.Popen(comando.lower())
            except FileNotFoundError:
                s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)
