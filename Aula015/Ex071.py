print('='*20, 'DESAFIO 071', '='*20)
print('='*30)
print('         BANCO CEV        ')
print('='*30)
saque=int(input('Qual valor você quer sacar? R$ '))
total = saque
ced=50
totalced = 0
while True:
    if total >=ced:
        total-=ced
        totalced+=1
    else:
        if totalced>0:
            print(f'Total de {totalced} cédulas de R$ {ced:2.2f}.')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totalced=0
        if total==0:
            break