print('='*20, 'DESAFIO 067', '='*20)

while True:
    print('-'*30)
    n=int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n<0:
        break
    for i in range(1, 10):
        print(f'{n} x {i} = {n*i}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')