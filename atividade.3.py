import os

os.system("cls")

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# Exemplo de uso
verificar_par_ou_impar(7)
verificar_par_ou_impar(12)