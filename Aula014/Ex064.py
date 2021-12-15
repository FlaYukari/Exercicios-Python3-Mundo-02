print('='*20, 'DESAFIO 064', '='*20)

n=0 # pode fazer n=cont=soma-0, dai tira as 2 linhas abaixo
cont=0
soma=0
while n!=999:
    n=int(input('Digite um número [999 para parar]: '))
    soma+=n
    cont+=1
cont=cont-1
soma=soma-999
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')