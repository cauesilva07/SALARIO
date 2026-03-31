import os

# Vetores do cardápio
codigos = [1, 2, 3, 4, 5]
pratos = ["Picanha", "Lasanha", "Strogonoff", "Bife Acebolado", "Pão com ovo"]
valores = [25.00, 20.00, 18.00, 15.00, 5.00]

# Vetores para armazenar os pedidos
pedidos = []
valores_pedidos = []

while True:
    print("\n--- Cardápio ---")
    for i in range(len(codigos)):
        print(f"{codigos[i]} - {pratos[i]} - R$ {valores[i]:.2f}")
    
    try:
        escolha = int(input("Escolha o código do prato desejado: "))
        if escolha in codigos:
            indice = codigos.index(escolha)
            pedidos.append(pratos[indice])
            valores_pedidos.append(valores[indice])
        else:
            print("Código inválido. Tente novamente.")
            continue
    except ValueError:
        print("Digite um número válido.")
        continue
    
    continuar = input("Deseja escolher outro prato? (s/n): ").lower()
    if continuar != 's':
        break

# Mostra os pedidos e o total
print("\n--- Seus pedidos ---")
total = 0
for i in range(len(pedidos)):
    print(f"{pedidos[i]} - R$ {valores_pedidos[i]:.2f}")
    total += valores_pedidos[i]

print(f"Total da conta: R$ {total:.2f}")
