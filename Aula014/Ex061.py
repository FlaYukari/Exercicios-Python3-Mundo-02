print('='*20, 'DESAFIO 061', '='*20)
#tem resolução com For ex051

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1= int(input('Primeiro Termo: '))
r=int(input('Razão: '))

n=0
while n<10:
    print(f'{a1+r*n} -> ', end='')
    n+=1
print('ACABOU')