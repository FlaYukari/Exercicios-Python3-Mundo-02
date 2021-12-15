print('='*20, 'DESAFIO 047', '='*20)

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou!\n')

print('Outro jeito de fazer:')
for n in range(1,51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou!')