import os

os.system("cls")

total = 0
opção = 0

while True:
    print("1 - Pizza (15,00)")
    print("2 - Lasanha (20,00)")
    print("3 - Strogonoff (18,00)")
    print("4 - Bife acebolado (25,00)")
    print("5 - Pão com ovo (5,00)")

    opção = int(input("Escolha um prato: "))

    if opção == 1:
        total += 15.00
    elif opção == 2:
        total += 20.00
    elif opção == 3:
        total += 18.00
    elif opção == 4:
        total += 25.00
    elif opção == 5:
        total += 5.00
    else:
        print("Opção inválida.")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break
            
print("Total da conta: R$ {:.2f}".format(total))
