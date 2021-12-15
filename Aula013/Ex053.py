print('='*20, 'DESAFIO 053', '='*20)

frase = str(input('Digite uma frase: '))

frase_junta=frase.replace(" ", "").upper()

frase_invertida=frase_junta[::-1]

print(frase_junta)
print(frase_invertida)

if frase_junta == frase_invertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

