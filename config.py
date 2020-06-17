

API_KEY = '1MAz2QY5_2MWLJwyyTMDhVPolvGtHeylEh6_8NZ3EUv8'
API_URL = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/05da4ef8-fb86-4e61-a5ed-ac19b9d8aec2'

# 0 passo inicial
# 1 morador
# 2 serviços
# 2.2 outros serviços
# 3 visitas
# 4 QRcode
# 5 Cadastro
# 6 Acessos
JORNADA = {
    '0': 'Olá, me fale de qual categoria você é, por favor',

    '1.1':'Você possui senha de acesso?',
    '1.1.1':'Deseja Falar com o Operador?',

    '2e3':'Por favor, fale o número do apartamento e o bloco',   
    '2e3.1':'Apartamento não encontrado, fale novamente',

    
    '2.1.1':'Fale umas das opções abaixo que melhor representa o tipo de serviço que você presta',
    '2.2': "Diga o seu tipo de serviço, por favor",
    '2.1.2': 'Morador está descendo para te receber',
    

    '5': 'Você possui cadastro?',
    '5.1': "Fique de frente para a câmera para que possamos identifica-lo",
    '5.2': "Apresente seu documento de RG ou CNH",
    '5.2.1':'Agora fique de frente para a câmera para cadastra sua foto no sistema',
    
    '6':'Acesso Liberado',
    '6.1': 'O morador está descendo para te receber',
    '3.1': 'Diga seu nome, por favor',
    '3.1.1':"Iremos avisar o morador da sua chegada",

    '4': 'Você possui QR côde para acesso?',
    '4.1': "Apresente seu QR côde",

    '5': 'Você possui cadastro?',
    '5.1': "Fique de frente para a câmera para que possamos identifica-lo",
    '5.2': "Apresente seu documento de RG ou CNH",
    '5.2.1':'Agora fique de frente para a câmera para cadastra sua foto no sistema',
    '5.2.2':'Cadastro realizado com sucesso',
    
    '6':'Acesso Liberado',
    
}

ANS = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'cento': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seiscentos': 600,
    'setecentos': 700,
    'oitocentos': 800,
    'novecentos': 900,
    'mil': 1000,
    'milhão': 1000000,
    'bilhão': 1000000000,
    'ponto': '.'
}