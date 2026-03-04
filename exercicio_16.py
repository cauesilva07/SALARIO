import os

os.system("cls")

sexo =(input("Digite o seu sexo:")) .lower()
ano_de_nascimento = int(input("Digite o teu ano de nascimento"))

idade = 2026 - ano_de_nascimento

idade_obrigatoria = idade >= 18
sexo_obrigatorio = sexo == "masculino"

if idade_obrigatoria and sexo_obrigatorio:
    print("Deve se apresentar ao serviço militar obrigatório!")
    
else:
    print("Não é necessário apresentar-se.")