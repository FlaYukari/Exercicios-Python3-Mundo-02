print('='*20, 'DESAFIO 040', '='*20)

n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))

m = (n1+n2)/2

print(f'Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {m:.2f}.')
if m<5:
    print('O aluno está REPROVADO.')
elif m>=7:
    print('O aluno está APROVADO.')
else:
    print('O aluno está em RECUPERAÇÃO.')