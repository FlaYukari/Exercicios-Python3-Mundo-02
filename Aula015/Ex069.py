print('='*20, 'DESAFIO 069', '='*20)

conth=0
contm=0
cont18=0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA     ')
    print('-'*30)
    while True:
        idade=input('Idade: ')
        if not idade.isdigit():
            print('Digite um número inteiro.')
        else:
            break
    while True:
        sexo=str(input('Sexo: [M/F] ').strip().upper())
        if sexo not in 'FM':
            print('Digite M/F.')
        else:
            break
    while True:
        perg=str(input('Quer continuar? [S/N] ').strip().upper())
        if perg not in 'SN':
            print('Digite S/N.')
        else:
            break
    if int(idade)>=18:
        cont18+=1
    if sexo == 'F' and int(idade)<20:
        contm+=1
    if sexo == 'M':
        conth+=1
    if perg =='N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {conth} homens cadastrados.')
print(f'E temos {contm} mulheres com menos de 20 anos.')
