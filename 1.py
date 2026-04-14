import os
from datetime import date, datetime
os.system("cls || clear")

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

ano = int(input("Digite o ano de nascimento: "))
idade_usuario = calcular_idade(ano)

print(f"Você tem {idade_usuario} anos.")