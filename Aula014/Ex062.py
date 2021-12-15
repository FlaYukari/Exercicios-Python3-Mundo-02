print('='*20, 'DESAFIO 062', '='*20)
# continuação do Ex061

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1= int(input('Primeiro Termo: '))
r=int(input('Razão: '))

termo=0
while termo<10:
    print(f'{a1+r*termo} -> ', end='')
    termo+=1
print('PAUSA\n')
a10=a1+(r*(termo-1))

termo1=int(input('Quantos termos você quer mostrar a mais? '))
elemento= 10+termo1
while termo1 !=0:
    i=1
    an=a10+r
    while i<=termo1:
        print(f'{(a10+r*(elemento-10-termo1)) + r * i} -> ',end='')
        i += 1
    print('PAUSA\n')
    termo1 = int(input('Quantos termos você quer mostrar a mais? '))
    elemento = elemento+termo1

print(f'\nProgressão finalizada com {elemento} termos mostrados.')