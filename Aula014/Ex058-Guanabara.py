print('='*20, 'DESAFIO 058', '='*20)

import random

print('Sou o seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n')

comp=random.randint(0,10)

acertou=False
palpite=0
while not acertou:
      jogador = int(input('Qual é seu palpite? '))
      palpite+=1
      if jogador ==comp:
            acertou=True
      else:
            if jogador>comp:
                  print('Menos...Tente mais uma vez')
            else:
                  print('Mais...Tente mais uma vez')
print(f'Acertou em {palpite} tentativas. Parabéns!')