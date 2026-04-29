import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: int
    Altura: int
    
paciente = Paciente(
    int(input('Digite a idade do paciente: ')), 
    input('Digite o nome do paciente: '),
    int(float(input('Digite o peso do paciente: '))),
    int(float(input('Digite a altura do paciente: ')))
)
print(f'Nome: {paciente.nome}')
print(f'Idade: {paciente.idade}')
print(f'Peso: {paciente.peso}')
print(f'Altura: {paciente.Altura}')
























