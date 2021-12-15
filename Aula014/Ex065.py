print('='*20, 'DESAFIO 065', '='*20)

cont=media=soma=0
lista=[]
resp='S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont+=1
    soma+=n
    lista.append(n)
    resp=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media=soma/cont
print(f'Você digitou {cont} números e a média foi {media}.\n'
      f'O maior valor foi {max(lista)} e o menor foi {min(lista)}.')
