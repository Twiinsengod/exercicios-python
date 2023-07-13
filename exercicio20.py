# Faça um programa que sorteia a ordem de apresentação de trabalhos dos alunos. Façum programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input('Primeiro(a) aluno(a): '))
n2 = str(input('Segundo(a) aluno(a): '))
n3 = str(input('Terceiro(a) aluno(a): '))
n4 = str(input('Quarto(a) aluno(a): '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)