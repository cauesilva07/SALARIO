Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
   primeira_nota, segunda_nota, terceira_nota, media: real

Inicio

   escreval("digite a primeira_nota: ")
   leia(primeira_nota)

   escreval("digite a segunda_nota: ")
   leia(segunda_nota)

   escreval("digite a terceira_nota: ")
   leia(terceira_nota)

   media <- primeira_nota + segunda_nota + terceira_nota / 2

   Se (media >= 7) Entao
      escreval( "parabens, aluno aprovado")
   Fimse

   Se (media < 7) Entao
      escreval( "que pena, aluno reprovado")
   Fimse


Fimalgoritmo