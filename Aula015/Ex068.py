print('='*20, 'DESAFIO 068', '='*20)

import random

print('=-'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*25)

cont=0
while True:
    eu=int(input('Digite um valor: '))
    resp=str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    comp=random.randint(0,10)
    t=eu+comp
    print('-'*56)
    print(f'Você jogou {eu} e o computador {comp}. Total de {t} ', end='')
    if t % 2==0:
        print('DEU PAR')
        print('-' * 56)
    else:
        print('DEU ÍMPAR')
        print('-' * 56)
    if (t%2!=0 and resp in 'P') or (t%2==0 and resp in 'I'):
        print('Você PERDEU!')
        print('=-'*26)
        break
    elif (t%2==0 and resp in 'P') or (t%2!=0 and resp in 'I'):
        print('Você VENCEU!')
        print('=-' * 26)
    print('Vamos jogar novamente...')
    cont+=1

print(f'GAME OVER! Você venceu {cont} vezes.')