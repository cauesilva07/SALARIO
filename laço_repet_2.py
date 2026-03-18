import os

os.system("cls")

QUANTIDADE_NOTAS = 3

soma = 0


for i in range(2):
  while True:
    nota = float(input("Digite uma nota: "))

    #if 0 <= nota <= 10:
     #   break
    #else:
     #   print("nota inválida! Tente novamente.")

#print("A nota informada foi:", nota)

#CALCULO DA MÉDIA
media = soma / QUANTIDADE_NOTAS

print(f"Média: {media}") 




