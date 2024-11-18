import requests

link =  'https://economia.awesomeapi.com.br/last/USD-BRL'

cotacao = requests.get(link).json()

def conv_brdol():
    real = float(input('\nDigite a quantia de Reais que deseja converter para Dólares: '))

    conv_br = real / float(cotacao['USDBRL']['bid'])
    print(f'O resultado da conversão é de U${round((conv_br),2)}')

def conv_dolbr():
    dolar = float(input('\nDigite a quantia de Dólares que deseja converter para Reais: '))

    con_dol = dolar * float(cotacao['USDBRL']['bid'])
    print(f'O resultado da conversão é de R${round((con_dol),2)}')

while True:
    print('Deseja converter sua moeda?')
    resposta = input('\nDigite: \n\t1 para sim \t2 para não\n\nResposta: ')
    if resposta == '1':
        break
    if resposta == '2':
        exit()

q_conv = input('Deseja converter:\n\t 1 = DÓLAR PARA REAL\t2 = REAL PARA DÓLAR\n\nResposta: ')

if q_conv == '1':
    conv_dolbr()

elif q_conv == '2':
    conv_brdol()




