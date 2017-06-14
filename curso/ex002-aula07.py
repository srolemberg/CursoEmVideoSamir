print('Olar! ' * 20)

nome = 'samir'
print('Testando Alinhamento: {:<20}!'.format(nome))  # : espacamento ||| < alinhado a esquerda
print('Testando Alinhamento: {:>10}!'.format(nome))  # : espacamento ||| > alinhado a direita
print('Testando Alinhamento: {:^15}!'.format(nome))  # : espacamento ||| ^ alinhado a centro
print('Testando Alinhamento: {:=^30}!'.format(
    nome))  # : espacamento ||| ˆ alinhado a centro ||| = preenche os vazios com iguais
