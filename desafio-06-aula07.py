# samir rolemberg, 2017
# curso em video
# desafio 03 aula 07
# crie um script que leia a largura e a altura de uma parede em metros e
# calcule sua area e a quantidade de tinta necessaria pra pintala
# sabendo que cada litro de tinta pinta uma area de 2m2

altura = float(input('informe a altura: '))
largura = float(input('informe a largura: '))

area = altura * largura

litros = area / (2 ** 2)

print('Sendo a Altura {} e a Largura {} a area de pintura será de {} metros'.format(altura, largura, area))
print('Serão necessários {} litros de tinta para pintar {} metros'.format(litros, area))
