print('='*20, 'DESAFIO 039', '='*20)

import datetime

ano=int(input('Ano de nascimento: '))

idade= datetime.date.today().year-ano

print(f'Quem nasceu em {ano} tem {idade} anos em {datetime.date.today().year}.')

if idade<18:
    print(f'Ainda faltam {18-idade} anos para o alistamento.\n'
          f'Seu alistamento será em {ano+ 18}.')
elif idade==18:
    print('Você deve se alistar IMEDIATAMENTE.')
else:
    print(f'Você já deveria ter se alistado há {idade-18} anos.\n'
          f'Seu alistamento foi em {ano + 18}.')
