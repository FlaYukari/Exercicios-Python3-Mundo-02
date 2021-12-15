print('='*20, 'DESAFIO 062', '='*20)
# continuação do Ex061

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

a1= int(input('Primeiro Termo: '))
r=int(input('Razão: '))

termo=a1
cont=1
total=0
mais=10

while mais !=0:
    total=total+mais
    while cont<=total:
        print(f'{termo} -> ',end='')
        termo+=r
        cont += 1
    print('PAUSA\n')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {total} termos mostrados.')