print('='*20, 'DESAFIO 054', '='*20)

import datetime

t_maior=0
t_menor=0
for ano in range(1, 8):
    nasc=int(input(f'Em que ano a {ano}ª pessoa nasceu? '))
    if (datetime.date.today().year-nasc)>=21:
        t_maior+=1
    else:
        t_menor+=1
print(f'Ao todo tivemos {t_maior} pessoas maiores de idade.\n'
      f'E também tivemos {t_menor} pessoas menores de idadae.')
