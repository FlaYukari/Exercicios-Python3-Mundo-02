print('='*20, 'DESAFIO 044', '='*20)

total=float(input('Preço das compras: R$ '))

forma_pgto=(int(input('FORMAS DE PAGAMENTO:\n'
                      '[ 1 ] à vista dinheiro/cheque\n'
                      '[ 2 ] à vista cartão\n'
                      '[ 3 ] 2x no cartão\n'
                      '[ 4 ] 3x ou mais no cartão\n'
                      'Qual opção? ')))

if forma_pgto == 1:
    print(f'\nSua compra de R$ {total:.2f} vai custar R$ {total*0.9:.2f} no final.')
elif forma_pgto==2:
    print(f'\nSua compra de R$ {total:.2f} vai custar R$ {total*0.95:.2f} no final.')
elif forma_pgto==3:
    print(f'\nSua compra será parecelada em 2x de R$ {total/2:.2f} SEM JUROS.\n'
          f'Sua compra vai custar R$ {total:.2f} no final.')
elif forma_pgto==4:
    parcelas=int(input('Quantas parcelas? '))
    total_juro=total*1.2
    parcela_juro=total_juro/parcelas
    print(f'\nSua compra será parcelada em {parcelas}x de R$ {parcela_juro:.2f} COM JUROS.\n'
          f'Sua compra de R$ {total:.2f} vai custar R$ {total_juro:.2f} no final.')
else:
    print(f'Essa opção {forma_pgto} não existe. \n'
          f'Tente novamente.')


