import os

os.system("cls")

import time

numero = int(input("Digite um número: "))

for numero in range(numero, -1, -1):
    print(numero)
    time.sleep(1) 