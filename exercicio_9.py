
import os

os.system("cls || clear")

quantidade = int(input("Digite a quantidade de maçãs : "))

if quantidade < 12:
    preço = 1

else:
    preço = 1.30

total = quantidade * preço

print("\n- Exibindo resultados -")

print(f"Preço por maçã: R$ {preço:.2f}")
print(f"Preço final: R$ {total:.2f}")
