import os
from dataclasses import dataclass

os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Categoria: {self.categoria}')
        print(f'Preço: R${self.preço:.2f}\n')


QUANTIDADE_LIVROS = 1
lista_livros = []

print('= Solicitando dados =')
for i in range(QUANTIDADE_LIVROS):
    novo_livro = Livro(
        nome=input('Digite o nome do livro: '),
        autor=input('Digite o nome do autor: '),
        categoria=input('Digite a categoria: '),
        preço=float(input("Digite o preço: "))
    )
    print('')
    lista_livros.append(novo_livro)

print('= Salvando dados =')
with open('contato_livros.csv', 'a', encoding='utf-8') as arquivo:
    for livro in lista_livros:
        arquivo.write(f'{livro.nome},{livro.autor},{livro.categoria},{livro.preço:.2f}\n')
print('Salvo com sucesso!\n')

print('= Consultando arquivo =')
with open('contato_livros.csv', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

print('= Fim do programa. =')