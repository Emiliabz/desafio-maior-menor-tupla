"""
DESAFIO: Maior e Menor Valores em Tupla
-------------------------------------------------------------------------
Enunciado:
Crie um programa que vai gerar cinco números aleatórios e colocar
dentro de uma tupla.

Depois disso, mostre:
A) A listagem de números gerados.
B) O menor valor que está na tupla.
C) O maior valor que está na tupla.

Destaques:
- Uso de random.randint para sorteio.
- Funções max() e min() para análise de dados.
-------------------------------------------------------------------------
"""

from random import randint


numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')


print(f'\nO maior valor sorteado foi \033[32m{max(numeros)}\033[m')
print(f'O menor valor sorteado foi \033[31m{min(numeros)}\033[m')