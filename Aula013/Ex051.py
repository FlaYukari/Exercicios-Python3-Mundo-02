print('='*20, 'DESAFIO 051', '='*20)
#tem resolução com While ex061

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1= int(input('Primeiro Termo: '))
r=int(input('Razão: '))
a11=a1+(r*10)

for c in range(a1,a11,r):
    print(f'{c} ', end='-> ')
print('ACABOU')