print('='*20, 'DESAFIO 052', '='*20)

num=int(input('Digite um número: '))

n_divisivel=0
for c in range(1,num+1):
    if num%c==0:
        print('\033[33m', end=' ')
        n_divisivel+=1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {n_divisivel} vezes.')

if n_divisivel ==2:
    print(f'O {num} é um número primo.')
else:
    print('E por isso ele NÃO É PRIMO.')


