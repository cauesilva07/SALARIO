import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Pessoa:
    nome: str
    idade: int


@dataclass
class Pet:
    nome: str
    idade: str

pessoa1 = Pessoa(nome='Aline', idade=30)
pessoa2 = Pessoa(nome='Júlia', idade=14)


pet1 = Pet(nome='Rex', idade='2 anos')
pet2 = Pet(nome='pandora', idade='1 ano')



print(f"Nome: {pessoa1.nome} \nIdade: {pessoa1.idade}")
print(f"Nome: {pet1.nome} \nIdade: {pet1.idade}")

print(f"Nome: {pessoa2.nome} \nIdade: {pessoa2.idade}")
print(f"Nome: {pet2.nome} \nIdade: {pet2.idade}")
