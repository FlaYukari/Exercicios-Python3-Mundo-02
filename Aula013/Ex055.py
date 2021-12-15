print('='*20, 'DESAFIO 055', '='*20)

peso=[]
for pessoa in range(1, 6):
    peso.append(float(input(f'Peso da {pessoa}ª pessoa: ')))

print(f'O maior peso lido foi de {max(peso)} Kg.\n'
      f'O menor peso lido foi de {min(peso)} Kg.')