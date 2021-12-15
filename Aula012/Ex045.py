print('='*20, 'DESAFIO 045', '='*20)

import time
import random
print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA\n')
j_pessoa=int(input('Qual é a sua jogada? '))

if j_pessoa<=2:
      print('JO')
      time.sleep(1)
      print('KEN')
      time.sleep(1)
      print('PO!!!')

      item=['Pedra', 'Papel', 'Tesoura']
      j_comp=random.randint(0, 2)

      print('-=-'*40)
      print(f'Computador jogou {item[j_comp]}.')
      print(f'Jogador jogou {item[j_pessoa]}.')
      print('-=-'*40)

      if j_comp==0: #comp jogou PEDRA
            if j_pessoa==0: #pessoa jogou PEDRA
                  print('EMPATE!')
            elif j_pessoa==1: #pessoa jogou PAPEL
                  print('JOGADOR GANHOU!')
            elif j_pessoa==2: #pessoa jogou TESOURA
                  print('COMPUTADOR GANHOU!')
      elif j_comp==1: #comp jogou PAPEL
            if j_pessoa==0: #pessoa jogou PEDRA
                  print('COMPUTADOR GANHOU!')
            elif j_pessoa==1: #pessoa jogou PAPEL
                  print('EMPATE!')
            elif j_pessoa==2: #pessoa jogou TESOURA
                  print('JOGADOR GANHOU!')
      elif j_comp==2:  #comp jogou TESOURA
            if j_pessoa==0: #pessoa jogou PEDRA
                  print('JOGADOR GANHOU!')
            elif j_pessoa==1: #pessoa jogou PAPEL
                  print('COMPUTADOR GANHOU!')
            elif j_pessoa==2: #pessoa jogou TESOURA
                  print('EMPATE!')
else:
      print('Jogada INVÁLIDA!')
