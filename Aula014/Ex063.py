print('='*20, 'DESAFIO 063', '='*20)

print('_'*25)
print('Sequencia de Fibonacci')
print('_'*25)

n=int(input('Quantos termos você quer mostrar? '))

if n == 1:
    print('0 -> FIM',
          end='')
    n -= 1
elif n == 2:
    print('0 -> 1 -> FIM',
          end='')
    n -= 2
elif n==0:
    print('FIM')
else:
    ele_ant = 1
    ele_ant_ant=0
    elemento = 0
    n=n-2
    while n >=1:
        print('0 -> 1 -> ',end='')
        while n>0:
            elemento= ele_ant + ele_ant_ant
            print(f'{elemento} -> ', end='')
            ele_ant_ant = ele_ant
            ele_ant=elemento
            n-=1
        break
    print('FIM')