import requests # importa a biblioteca requests

LINK = 'https://economia.awesomeapi.com.br/last/USD' # LINK armazena o link GET da API de Cotações

REQ = requests.get(LINK) # armazena a requisição pra pegar o link
REQ = REQ.json() # transforma o link em json, para o python ler --> DICIONARIO

def pegar_alta_dolar(dicionario=REQ['USDBRL']): # pega o dicionario como dolar em REQ
    for chave in dicionario: # para cada chave do dicionario
        if chave == 'high': # se a chave for high - alta
             valor = dicionario[chave] # valor armazena o valor da alta
             return float(valor) # retorna o valor como float

def pegar_baixa_dolar(dicionario=REQ['USDBRL']):
    for chave in dicionario:
        if chave == 'low': # se a chave for low - baixa
             valor = dicionario[chave] # valor armazena o valor da baixa
             return float(valor) # retorna como float 

# faz a média da alta e da baixa, e retorna um dolar em real       
def converter_um_dolar_em_real(alta=pegar_alta_dolar(), baixa=pegar_baixa_dolar()):  
    return (alta + baixa) / 2

# pega 1 real e divide pelo valor de um dolar em reais, retornando um real em dolar 
def converter_um_real_em_dolar(um_dolar=converter_um_dolar_em_real()):
    return 1 / um_dolar

# pega um dolar em real, e multiplica pela quantidade de dólares passada pelo usuário
# retorna a qtd de dolares em reais
# ex. 14/04/2024 --> (R$ 5.12) X (USD 2.00) --> (R$ 10.24)
def converter_dolares_em_reais(dolares, um_dolar=converter_um_dolar_em_real()):
    return um_dolar * dolares

# pega um real em dolar, e multiplica pela quantidade de reais passada pelo usuário
# retorna a qtd de reais em dolares
# ex. 14/04/2024 --> (USD 0.20) X (R$10.24) --> (USD 2.00)
def converter_reais_em_dolares(reais, um_real=converter_um_real_em_dolar()):
    return um_real * reais
