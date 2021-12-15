print('='*20, 'DESAFIO 053 - Resolvido pelo Guanabara', '='*20)

frase = str(input('Digite uma frase: ')).strip().upper() # .strip retira os espaços no início e no final da frase.
# .upper deixou todas as letras maiúsculas.

palavras =frase.split() # transforma a frase em uma lista de palavras. Transformou em um VETOR!
#print(palavras)

junto=''.join(palavras) # juntou todas as palavras.
print(junto)

junto_invert=''
for letra in range(len(junto)-1, -1, -1):
    junto_invert+=junto[letra]
print(junto_invert)

if junto == junto_invert:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

