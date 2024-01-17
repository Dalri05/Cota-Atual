import requests
from os import system
from time import sleep

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes ["USDBRL"]["bid"]
cotacao_euro = cotacoes["EURBRL"]["bid"]
cotacao_btc = cotacoes["BTCBRL"]["bid"]


def menu():
    system("DATE /T")
    system("color 4")
    print(''' 
    [1] - Dolar
    [2] - Euro
    [3] - Bitcoin
    ''')
    op = int(input("Digite a opção desejada:"))

    if op == 1:
        print("O valor do dolar é de", cotacao_dolar, "reais")
        sleep(5)
        system("cls")
        menu()
    elif op == 2:
        print("O valor do euro é de",cotacao_euro, "reais")
        sleep(5)
        system("cls")
        menu()
    elif op == 3:
        print("O valor do bitcoin é de",cotacao_btc,"reais")
        sleep(5)
        system("cls")
        menu()
    else:
        print("opção incorreta, aguarde 3 segundos...")
        sleep(3)
        system("cls")
        menu()
menu()