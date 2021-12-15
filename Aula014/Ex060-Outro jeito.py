print('='*20, 'DESAFIO 060 - Outro Jeito', '='*20)

num=int(input('Digite um número para calcular seu Fatorial: '))
c=num
f=1
print(f'\nCalculando {num}! = ', end='')
while c>0:
    print(f'{c}', end='')
    print(' x ' if c>1 else ' = ', end='')
    f=f*c
    c-=1
print(f'{f}.')