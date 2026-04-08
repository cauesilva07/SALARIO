def calcular_idade(ano_nascimento):
    ano_atual = 2026  # Ano atual
    idade = ano_atual - ano_nascimento
    return idade

# Solicita ao usuário o ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Chama a função e exibe a idade
idade = calcular_idade(ano_nascimento)
print(f"Sua idade é {idade} anos.")