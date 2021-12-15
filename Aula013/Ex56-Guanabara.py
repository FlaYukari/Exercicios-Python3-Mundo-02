print('='*20, 'DESAFIO 056 - com ajuda do Guanabara', '='*20)
somaidade=0
sexo_m=0
sexo_f=0
idade_f=0
for pessoas in range(1,5):
    print(f'----- {pessoas}ª PESSOA -----')
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo= str(input('Sexo [M/F]: ')).strip().upper()
    somaidade+=idade
    idade_m=[]
    if sexo=='Mm':
        idade_m.append(idade)

    else:
        sexo_f+=1
        if idade<20:
            idade_f+=1
mais_velho = max(idade_m)
media_idade=somaidade/4
print(f'A média de idade do grupo é de {media_idade:.2f} anos.\n')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome}.\n')
print(f'Ao todo são {idade_f} mulheres com menos de 20 anos.')

