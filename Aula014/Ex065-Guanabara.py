print('='*20, 'DESAFIO 065', '='*20)

cont=media=soma=maior=menor=0
resp='S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont+=1
    soma+=n
    if n==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media=soma/cont
print(f'Você digitou {cont} números e a média foi {media}.\n'
      f'O maior valor foi {maior} e o menor foi {menor}.')
