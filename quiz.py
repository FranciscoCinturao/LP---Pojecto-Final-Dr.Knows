import time
import telepot
from telepot.namedtuple import KeyboardButton,ReplyKeyboardMarkup
import telepot as t
#attention : dont change array '' in lists.
k=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Começar Quiz')]])
k1=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Tentar de novo')]])
start=0
lis=['']
lis1=['',
      'Não é uma vantagem do SGBD?',
      'As diversas funções do SGBD não incluem..',
      'O uso de um SGBD NÃO é necessário para..',
      'Escolhe a alternativa que reúne as vantagens no uso de um SGBD',
      'O projeto de uma base de dados divide-se em várias fases. Nesse contexto, é elaborado o Modelo Entidade-Relacionamento (MER) como resultado do(a)... ',
      'Um dos objetivos da normalização de dados é..',
      'Com base nos conhecimentos acerca da arquitetura de três camadas de um SGBD, analise a seguinte frase: “É a capacidade de alterar o esquema físico sem precisar modificar os esquemas lógico ou conceitual”. Esse conceito refere-se à: ',
      'Um conjunto importante de propriedades das transações em uma base de dados recebe oacrônimo ACID. O significado de ACID é:',
      'Indique em quais das situações abaixo é mais indicado usar SGBDs',
      'Os programas PL/SQL são compostos por blocos. Assim, quais das palavras chaves abaixo são usadas para definir um bloco?']#strings are the questions
lis2=['',ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Controle de Redundância'),KeyboardButton(text='Compartilhamento de dados')],[KeyboardButton(text='Restrição a acesso não autorizado'),KeyboardButton(text='Custo')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Definição e a manipulação de dados'),KeyboardButton(text='A otimização do uso de dados')],[KeyboardButton(text='Gestão e a otimização de ficheiros'),KeyboardButton(text='Garantia da segurança e integridade de dados')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Gerir base de dados simples onde não há reconhecidamente múltiplos acessos'),KeyboardButton(text='Controlar de Redundância')],[KeyboardButton(text='Restringir o acesso não autorizado dos dados'),KeyboardButton(text='Manter de Restrições de Integridade na BD')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Rastreabilidade'),KeyboardButton(text='Dispersão e facilidade de programação')],[KeyboardButton(text='Facilidade de implementações semânticas'),KeyboardButton(text='Segurança')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Coleta e análise de requisitos'),KeyboardButton(text='Projeto conceitual')],[KeyboardButton(text='Projeto lógico'),KeyboardButton(text='Projeto físico')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Minimizar a redundância de dados'),KeyboardButton(text='Melhorar o desempenho de consultas que envolvem grandes volumes de dados')],[KeyboardButton(text='Preparar uma base de dados para ser usada em aplicações OLAP'),KeyboardButton(text='Permitir a restauração de uma base de dados em caso de falha')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Independência de programação'),KeyboardButton(text='Independência física')],[KeyboardButton(text='Independência lógica'),KeyboardButton(text='Independência do Sistema Operativo')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Atomicidade, Consistência, Isolamento e Durabilidade'),KeyboardButton(text='Atenção, Consistência, Independência e Disponibilidade')],[KeyboardButton(text='Atomicidade, Concorrência, Independência e Durabilidade.'),KeyboardButton(text='Atomicidade, Concorrência, Isolamento, Disponibilidade')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Usar funções específicas, não suportadas pela linguagem de consulta, para tratar dos dados'),KeyboardButton(text='Acesso eficiente aos dados em aplicações de tempo real')],[KeyboardButton(text='Quando não há necessidade de garantir a segurança dos dados'),KeyboardButton(text='Quando a base de dados é simples e utilizada por um único utilizador')]]),
      ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='OPEN - BEGIN – EXCEPTION - CLOSE'),KeyboardButton(text='DECLARE - BEGIN – END - CLOSE')],[KeyboardButton(text='DECLARE - BEGIN – EXCEPTION - END'),KeyboardButton(text='BEGIN – OPEN - CLOSE - END')]])
      ]
# about lis2 : strings are choices(to answer)
lis3=[  '',
        'Custo',
        'Gestão e a otimização de ficheiros',
        'Gerir base de dados simples onde não há reconhecidamente múltiplos acessos',
        'Segurança',
        'Coleta e análise de requisitos',
        'Minimizar a redundância de dados.',
        'Independência lógica',
        'Atomicidade, Consistência, Isolamento e Durabilidade',
        'Acesso eficiente aos dados em aplicações de tempo real',
        '-DECLARE - BEGIN – EXCEPTION - END']#list of right answers
start_time=None
def main(ms):
    global lis
    global start
    global start_time
    i=ms['chat']['id']
    c=ms['text']
    ##print(ms['from']['user'],' : ')
    print(c)
    if c=='/start' or c=='Começar Quiz':
        bot.sendMessage(i,'Vamos começar o Quiz!',reply_markup=k)#name of test
    if c=='Começar Quiz' or c=='Tentar de novo':
        start=1
        start_time=time.process_time()
    if start and start<12:#number of questions-2
        if c!='Começar Quiz' and c!='Tentar de novo':
            lis.append(c)
        if start<11:
            bot.sendMessage(i,lis1[start],reply_markup=lis2[start])
        else:
            end_time=time.process_time()
            timer=int(end_time-start_time)
            start=0
            co=0
            no=-1
            for i in lis:
                if i==lis3[co]:
                    no=no+1
                co=co+1
            timerer=timer
            if timer>=70:#note : formula can be changed depends on hardness and number of question
                final_score=no*5
            else:
                if timer<30:
                    timer=30
                final_score=no*(70-timer)/4
            if final_score>100:
                final_score=100
            lis=['']
            bot.sendMessage(ms['chat']['id'],'Tempo : '+str(int(timerer))+' segundos \n Repostas correctas : '+str(no)+'/10 \n Resultado Final : '+str(int(final_score))+'/100',reply_markup=k1)
        if start!=0:
            start=start+1
bot=t.Bot('740178595:AAFDG9LLH7h5JadIsE9hqJe_RZRiQxHNGMw')
bot.message_loop(main)
while True:
    s=1
