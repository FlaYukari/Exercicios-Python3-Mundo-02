print('='*20, 'DESAFIO 056', '='*20)

soma_idade=0
for dados in range(1,5):
    print(f'----- {dados} PESSOA -----')
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade+=idade

media=soma_idade/4
print(f'A média de idade do grupo é de {media} anos.\n')

if sexo in 'Mm':

'O homem mais velho tem {} anos e se chama Cláudio.\n'
'Ao todo são {} mulheres com menos de 20 anos.'