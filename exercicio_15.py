import os

os.system("cls")

nota = float(input("Digite a nota: "))
if 0 <= nota <= 10: 
    print("Nota informada:", nota)
else: 
    print("A nota deve ser de zero a dez.")