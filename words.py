from telepot.namedtuple import KeyboardButton, ReplyKeyboardMarkup

words = {
    "PT": {
        "hello": "Olá",
        "notyou": "Tu já estás",
        "waiting4all": "Faltam jogadores",
        "understand": 'Desculpa, não percebi. Podes formular a pergunta de outra forma?',
        "quiz_wel": "Vamos começar o Quiz!",
        "stop": "Obrigado por participares nas minhas actividades!",
        "no_user": "Esse utilizador não existe!",
        "main_start": "Bem-vindo de volta!",
        "welcome": "Bem-vindo! Eu sou o Dr.Knows e estou aqui para te ajudar a aprender sobre base de dados. Por favor, escolhe a tua linguagem",
        "selectlang": "Escolha o seu idioma",
        "time": "Tempo: ",
        "sec": " segundos",
        "truerec": "Repostas correctas: ",
        "finalprog": "Resultado Final: ",
        "or": " ou ",
        "typq": "Existem os seguintes tipos de resposta:",
        "respo": "Qual a resposta que pretende?",
        "KB": {
            "main": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Portugu\u00EAs'), KeyboardButton(text='English')]]),
            "k": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Começar Quiz')]]),
            "dubble": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Quiz'), KeyboardButton(text='Selecione disciplina'), KeyboardButton(text='Selecione linguagem')]]),
            "clear": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=' ')]]),
            "k1": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Tentar de novo'), KeyboardButton(text='/stop')]]),
            "selecione disciplina": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='MBD'), KeyboardButton(text='ABD')]]),
            "select subject": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='ADB'), KeyboardButton(text='MDB')]])
        },
        "lis1": [
            '',
            'Não é uma vantagem do SGBD?',
            'As diversas funções do SGBD não incluem..',
            'O uso de um SGBD NÃO é necessário para..',
            'Escolhe a alternativa que reúne as vantagens no uso de um SGBD',
            'O projeto de uma base de dados divide-se em várias fases. Nesse contexto, é elaborado o Modelo Entidade-Relacionamento (MER) como resultado do(a)... ',
            'Um dos objetivos da normalização de dados é..',
            'Com base nos conhecimentos acerca da arquitetura de três camadas de um SGBD, analise a seguinte frase: “É a capacidade de alterar o esquema físico sem precisar modificar os esquemas lógico ou conceitual”. Esse conceito refere-se à: ',
            'Um conjunto importante de propriedades das transações em uma base de dados recebe o acrônimo ACID. O significado de ACID é:',
            'Indique em quais das situações abaixo é mais indicado usar SGBDs',
            'Os programas PL/SQL são compostos por blocos. Assim, quais das palavras chaves abaixo são usadas para definir um bloco?'
        ],  # strings are the questions
        "lis2": ['', ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Controle de Redundância'), KeyboardButton(text='Compartilhamento de dados')], [KeyboardButton(text='Restrição a acesso não autorizado'), KeyboardButton(text='Custo')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Definição e a manipulação de dados'), KeyboardButton(text='A otimização do uso de dados')], [
                                     KeyboardButton(text='Gestão e a otimização de ficheiros'), KeyboardButton(text='Garantia da segurança e integridade de dados')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Gerir base de dados simples onde não há reconhecidamente múltiplos acessos'), KeyboardButton(
                     text='Controlar de Redundância')], [KeyboardButton(text='Restringir o acesso não autorizado dos dados'), KeyboardButton(text='Manter de Restrições de Integridade na BD')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Rastreabilidade'), KeyboardButton(text='Dispersão e facilidade de programação')], [
                                     KeyboardButton(text='Facilidade de implementações semânticas'), KeyboardButton(text='Segurança')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Coleta e análise de requisitos'), KeyboardButton(
                     text='Projeto conceitual')], [KeyboardButton(text='Projeto lógico'), KeyboardButton(text='Projeto físico')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Minimizar a redundância de dados'), KeyboardButton(text='Melhorar o desempenho de consultas que envolvem grandes volumes de dados')], [
                                     KeyboardButton(text='Preparar uma base de dados para ser usada em aplicações OLAP'), KeyboardButton(text='Permitir a restauração de uma base de dados em caso de falha')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Independência de programação'), KeyboardButton(text='Independência física')], [
                                     KeyboardButton(text='Independência lógica'), KeyboardButton(text='Independência do Sistema Operativo')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Atomicidade, Consistência, Isolamento e Durabilidade'), KeyboardButton(text='Atenção, Consistência, Independência e Disponibilidade')], [
                                     KeyboardButton(text='Atomicidade, Concorrência, Independência e Durabilidade.'), KeyboardButton(text='Atomicidade, Concorrência, Isolamento, Disponibilidade')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Usar funções específicas, não suportadas pela linguagem de consulta, para tratar dos dados'), KeyboardButton(text='Acesso eficiente aos dados em aplicações de tempo real')], [
                                     KeyboardButton(text='Quando não há necessidade de garantir a segurança dos dados'), KeyboardButton(text='Quando a base de dados é simples e utilizada por um único utilizador')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='OPEN - BEGIN – EXCEPTION - CLOSE'), KeyboardButton(text='DECLARE - BEGIN – END - CLOSE')], [
                                     KeyboardButton(text='DECLARE - BEGIN – EXCEPTION - END'), KeyboardButton(text='BEGIN – OPEN - CLOSE - END'), KeyboardButton(text='/stop')]])
                 ],
        "lis3": [
            'Custo',
            'Gestão e a otimização de ficheiros',
            'Gerir base de dados simples onde não há reconhecidamente múltiplos acessos',
            'Segurança',
            'Coleta e análise de requisitos',
            'Minimizar a redundância de dados',
            'Independência lógica',
            'Atomicidade, Consistência, Isolamento e Durabilidade',
            'Acesso eficiente aos dados em aplicações de tempo real',
            'DECLARE - BEGIN – EXCEPTION - END'
        ],
        "abd": [
            "Pergunta 1",
            "Pergunta 2",
            "Pergunta 4"
        ],
        "mbd": " - Base de dados\n - Modela\u00E7\u00E3o de base de dados\n - Dados\n - Guardar dados \n - Abstra\u00E7\u00E3o na base de dados \n - Independ\u00eancia dados \n - Ficheiro heap \n - Ficheiro hash \n",
        "abd": " - Fun\u00E7\u00f5es \n - Exce\u00e7\u00f5es pl/sql \n - Par\u00e2metros utilizados nas fun\u00e7\u00f5es \n - Tipos dados \n - Armazenamento bases de dados \n - Arquiteturas das SGBDS \n - Constitui\u00e7\u00e3o Aplica\u00E7\u00E3o base dados",
    },
    "EU": {
        "hello": "Hello",
        "notyou": "You're already ready!",
        "waiting4all": "Some players yet to join",
        "understand": 'I did not understand, sorry! Can you ask with some different words? :)',
        "quiz_wel": "Let's start the Quiz! Get ready, champ!",
        "stop": "Thank you for participating on my activities!!",
        "no_user": "There is no such user!",
        "main_start": "Welcome again, friend :)",
        "welcome": "Hi! Welcome, i'm Dr.Knows, pleasure to meet you! Please choose your language to proceed",
        "selectlang": "Choose your language",
        "time": "Time: ",
        "sec": " seconds",
        "truerec": "Correct answers: ",
        "finalprog": "Final score: ",
        "or": " or ",
        "typq": "There are the following types of questions:",
        "respo": "What is the type of answer you wish?",
        "KB": {
            "main": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Portugu\u00EAs'), KeyboardButton(text='English')]]),
            "k": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Start Quiz')]]),
            "dubble": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Quiz'), KeyboardButton(text='Subject selection'), KeyboardButton(text='Language selection')]]),
            "clear": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=' ')]]),
            "k1": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Try again'), KeyboardButton(text='/stop')]]),
            "select subject": ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='MDB'), KeyboardButton(text='ADB')]])
        },
        "lis1": [
            "Isn't it an advantage of DBMS?",
            'The various functions of the DBMS do not include ..',
            'The use of a DBMS is NOT necessary for ..',
            'Choose the alternative that combines the advantages of using a DBMS',
            'The design of a database is divided into several phases. In this context, the Entity-Relationship Model (MER) is developed as a result of (a) ...',
            'One of the goals of data normalization is ..',
            'Based on the knowledge about the three-layer architecture of a DBMS, analyze the following sentence: "It is the ability to change the physical scheme without having to modify the logical or conceptual schemes". This concept refers to:',
            'An important set of transaction properties in a database is given the acronym ACID. The meaning of ACID is:',
            'Indicate in which of the situations below it is best to use DBMSs',
            'PL / SQL programs are composed of blocks. So, which of the keywords below are used to define a block?'
        ],  # strings are the questions
        "lis2": ['', ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Redundancy Control'), KeyboardButton(text='Data sharing')], [KeyboardButton(text='Restriction to unauthorized access'), KeyboardButton(text='Cost')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Definition and manipulation of data'), KeyboardButton(text='Optimizing data usage')], [
                                     KeyboardButton(text='File management and optimization'), KeyboardButton(text='Ensuring data security and integrity')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Manage a simple database where multiple accesses are not recognized'), KeyboardButton(
                     text='Control of Redundancy')], [KeyboardButton(text='Restrict unauthorized access to data'), KeyboardButton(text='Maintain Integrity Restrictions on BD')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Traceability'), KeyboardButton(text='Dispersion and ease of programming')], [
                                     KeyboardButton(text='Ease of semantic implementations'), KeyboardButton(text='Safety')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Requirements collection and analysis'), KeyboardButton(
                     text='Conceptual design')], [KeyboardButton(text='Logical design'), KeyboardButton(text='Physical design')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Minimize data redundancy'), KeyboardButton(text='Improve the performance of queries involving large volumes of data')], [
                                     KeyboardButton(text='Prepare a database for use in OLAP applications'), KeyboardButton(text='Allow the restoration of a database in case of failure')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Schedule independence'), KeyboardButton(text='Physical independence')], [
                                     KeyboardButton(text='Logical independence'), KeyboardButton(text='Operating System Independence')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Atomicity, Consistency, Isolation and Durability'), KeyboardButton(text='Attention, Consistency, Independence and Availability')], [
                                     KeyboardButton(text='Atomicity, Competition, Independence and Durability.'), KeyboardButton(text='Atomicity, Competition, Isolation, Availability')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Use specific functions, not supported by the query language, to handle the data'), KeyboardButton(
                     text='Efficient access to data in real-time applications')], [KeyboardButton(text='When there is no need to guarantee data security'), KeyboardButton(text='When the database is simple and used by a single user')]]),
                 ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='OPEN - BEGIN – EXCEPTION - CLOSE'), KeyboardButton(text='DECLARE - BEGIN – END - CLOSE')], [
                                     KeyboardButton(text='DECLARE - BEGIN – EXCEPTION - END'), KeyboardButton(text='BEGIN – OPEN - CLOSE - END'), KeyboardButton(text='/stop')]])
                 ],
        "lis3": [
            'Cost',
            'File management and optimization',
            'Manage a simple database where multiple accesses are not recognized',
            'Safety',
            'Requirements collection and analysis',
            'Minimize data redundancy.',
            'Logical independence',
            'Atomicity, Consistency, Isolation and Durability',
            'Efficient access to data in real-time applications',
            'DECLARE - BEGIN – EXCEPTION - END'
        ],
        "abd": [
            "Pergunta 1",
            "Pergunta 2",
            "Pergunta 4"
        ],
        "mdb": " - Modeling database \n - Data \n - Database management system \n - Store data \n  - Levels of abstraction in a dbms \n - Data independence \n - Kinds of data independence \n - Heap files \n - Sorted files \n - Hashed files",
        "adb": " - Functions \n - Exceptions\n - Parameters \n - Types of data\n - SGBD architecture \n - Constitution database application",
    }
}
