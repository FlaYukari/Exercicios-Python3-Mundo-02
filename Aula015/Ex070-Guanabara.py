print('='*20, 'DESAFIO 070', '='*20)
total=tot1000= menorpreco= cont=0
barato= ''

while True:
    produto=str(input('Nome do Produto: '))
    preco=float(input('Preço: R$ '))
    cont+=1
    total+=preco
    if cont==1 or preco<menorpreco: # acrescentou o or porque os comandos do if prec<menorpreco são os mesmos.
        menorpreco=preco
        barato=produto
    # else:
    #     if preco<menorpreco:
    #         menorpreco=preco
    #         barato = produto
    if preco >=1000:
        tot1000+=1

    resp=' '
    while resp not in "SN":
        resp=str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if resp == 'N':
        break

print(f'O total da compra foi {total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} custa R$ {menorpreco:.2f}.')