print('='*20, 'DESAFIO 048', '='*20)

soma=0
cont=0
for n in range(1, 501):
    if n%3==0 and n%2!=0:
        cont+=1
        soma+=n
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
