print('='*20, 'DESAFIO 058', '='*20)

import random

print('Sou o seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n')

comp=random.randint(0,20)

acertou=False
palpite=int(input('Qual é seu palpite? '))

if comp==palpite:
      print(f'Acertou com 1 tentativa. PARABÉNS!')
else:
      while palpite!=comp:
            tentativa=1
            if palpite == comp:
                  print(f'Acertou com {tentativa} tentativas. Parabéns!')
            elif palpite>comp:
                  print('Menos...', end='')
            else:
                  print('Mais...', end='')
            palpite=int(input('Qual o seu palpite? '))
            tentativa+=1
