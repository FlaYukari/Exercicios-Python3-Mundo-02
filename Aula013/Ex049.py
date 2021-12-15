print('='*20, 'DESAFIO 049', '='*20)

a=int(input('Digite um número para ver sua tabuada: '))
n=1
for n in range(1,11):
    print(f'{a} x {n:2} = {n*a:2}')

print('OU...')
for n in range(1,11):
    print(f'{a} x {n:2} = {a*n:2}')