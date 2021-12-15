print('='*20, 'DESAFIO 041', '='*20)
import datetime

nasc=int(input('Ano de nascimento: '))

idade = datetime.date.today().year - nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')