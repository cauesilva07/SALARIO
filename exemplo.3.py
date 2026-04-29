import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

cliente1 = Cliente(nome='Aline', email='aline@gmail.com' , telefone='11999999999'   )

print(f'Nome: {cliente1.nome}')
print(f'Email: {cliente1.email}')
print(f'Telefone: {cliente1.telefone}')