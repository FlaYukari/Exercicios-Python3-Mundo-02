print('='*20, 'DESAFIO 043', '='*20)

peso = float(input('Qual é seu peso? (Kg) '))

altura = float(input('Qual a sua altura? (m) '))

imc=peso/(altura**2)

print(f'O IMC dessa pessoa é de {imc:.2f}.')

if imc<18.5:
    print('Você está ABAIXO DO PESO NORMAL.')
elif imc<25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc<30:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')