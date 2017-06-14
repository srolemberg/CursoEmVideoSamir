# samir rolemberg, 2017
# curso em video
# desafio 03 aula 07
# crie um script que leia um numero e mostre sua tabuada

valor = int(input('informe um numero: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(valor, i, i * valor))
