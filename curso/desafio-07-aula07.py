# samir rolemberg, 2017
# curso em video
# desafio 03 aula 07
# crie um script que leia oo preco de um produto e mostre seu novo precom com %5 de desconto
preco = float(input('informe o preço: '))

print('O preço do produto é: {}'.format(preco))
print('O desconto foi de {}'.format(preco * 0.05))
print('O valor final é de: {}'.format(preco - (preco * 0.05)))
