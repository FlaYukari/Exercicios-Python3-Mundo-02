print('='*20, 'DESAFIO 070', '='*20)
total=preco1=preco=cont1000=precobarato=0
produto1=produto=produtobarato= ''
while True:
    produto1=str(input('Nome do Produto: '))
    while True:
        preco1=input('Preço: R$ ')
        if preco1.isdigit():
            break
        if float(preco1)>1000:
            cont1000+=1
    total+=float(preco1)
    if produto1 != '' and preco1 !='':
        produto = str(input('Nome do Produto: '))
        while True:
            preco = input('Preço: R$ ')
            if preco.isdigit():
                break
        total += float(preco)
        if float(preco1)<float(preco):
            precobarato=preco1
            produtobarato=produto1
        if preco<preco1:
            precobarato=preco
            produtobarato=produto
        if preco > 1000:
            cont1000 += 1
        total+=preco

    while True:
        perg=str(input('Quer continuar? [S/N] ').strip().upper()[0])
        if perg in 'SN':
            break
    if perg=='N':
        break

print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos {cont1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtobarato} que custa R$ {precobarato:.2f}.')