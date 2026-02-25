import os
os.system("cls") 

print("- Solicitando dados -")
primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite um número: ")) 

#calculando
produto = primeiro_numero * segundo_numero
soma = primeiro_numero + segundo_numero
media = soma / 2
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print("\n- Exibindo resultados:- ")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Produto: {produto}")

if primeiro_numero == segundo_numero:
    print("Os números são iguais.")

else:
    print("Os números não são iguais.") 