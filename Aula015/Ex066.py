print('='*20, 'DESAFIO 066', '='*20)
# desafio 064

cont=soma=0
while 'true':
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma+=n
    cont +=1
print(f'A soma dos {cont} valores foi {soma:.2f}!')