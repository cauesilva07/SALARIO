import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Funcionario:
    nome: str
    email: str
    matricula: str
    setor: str

funcionario1 = Funcionario(nome='Richard', email='richard@gmail.com'  , matricula='3456' , setor='operador de maquinas' )

print(f'Nome: {funcionario1.nome}')
print(f'Email: {funcionario1.email}')
print(f'Matricula: {funcionario1.matricula}')
print(f'Setor: {funcionario1.setor}')



