print('='*20, 'DESAFIO 046', '='*20)

import time

print('Contagem regressiva para o estouro de fogos de artifício!')
time.sleep(2)
print('Começando no 10...')
time.sleep(1)
for cont in range(9,-1,-1):
    print(cont)
    time.sleep(1)

print('BUM! BUM! POWW!')