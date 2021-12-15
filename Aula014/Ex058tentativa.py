print('='*20, 'DESAFIO 058', '='*20)

import random

print('Sou o seu computador...\n'
      'Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?\n')
palpite=int(input('Qual é seu palpite? '))

comp = random.randint(0,10)

if comp == palpite:
      print(f'Acertou com 1 tentativa. PARABÉNS!')
else:
      tentativa = 1
      if palpite !=comp:
            if palpite>comp:
                  print('Menos...')
            else:
                  print('Mais...')
            tentativa=int(input('Tente mais uma vez: '))
            tentativa+=1
      else:
            print(f'Acertou com {tentativa} tentativas. Parabéns!')
