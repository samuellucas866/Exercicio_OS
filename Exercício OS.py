# Função para impressão de Protocolo
import random


def NumeroProtocolo():
    return random.randint(1, 1000)



print("Bem-Vindo ao Sistema de OS")

control = True

while control:
    input("Insira o nome da empresa: ")
    input("Insira o CNPJ: ")
    input("Insira o nome do responsável: ")
    input("Insira o Setor: ")
    input("Insira um número para contato:")
    operador = int(
        input("Escolha o tipo de serviço: \n 1) Instalação \n 2) Manutenção \n 3) Visita Técnica \n 4)Outros \n R.:"))

    if operador == 1:
        print(NumeroProtocolo())

    if operador == 2:
        print(NumeroProtocolo())

    if operador == 3:
        print(NumeroProtocolo())

    if operador == 4:
        input("Informe sua dúvida ou informação que deseja receber e entraremos em contato: ")
        print(NumeroProtocolo())

    if operador == 5:
        print("Favor escolha uma opção válida!")

    control2 = input("Deseja continuar no Sistema? \n S/N \n R.: ")
    if control2.upper() == "S":
        control = True

    else:
        control = False
