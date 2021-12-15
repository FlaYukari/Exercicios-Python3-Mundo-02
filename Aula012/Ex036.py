print('='*20, 'DESAFIO 036', '='*20)

casa = float(input('Valor da Casa: '))

salario = float(input('Salário do comprador: R$ '))

anos = float(input('Quantos anos de financiamento? '))

prestacao = (casa)/(anos*12)

autorizado = 0.3*(salario)

print(f'Para pagar uma casa de {casa:.2f} em {anos} a prestação será de R$ {prestacao:.2f}.')
if prestacao<=(0.3*salario):
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')