# samir rolemberg, 2017
# curso em video
# desafio 03 aula 07
# crie um script que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere 1.00 US = 3.27 RS

golpes = 3.27
# muros = 1.0
dinheiros = float(input('informe quantos Reais (golpes) você tem: '))

print('Com a quantia de R$: {} Golpes você pode adquirir U$: {} muros'.format(dinheiros, dinheiros / golpes))
