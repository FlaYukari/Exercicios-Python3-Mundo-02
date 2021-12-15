print('='*20, 'DESAFIO 042', '='*20)

p=float(input('Primeiro seguimento: '))
s=float(input('Segundo seguimento: '))
t=float(input('Terceiro seguimento: '))

if p<(s+t) and s<(p+t) and t<(p+s):
    print('Os seguimentos acima PODEM FORMAR triângulo ', end= '')
    if p!=s!=t!=p: #cuidado!!!! o p tem q ser diferente do t também....
        print('ESCALENO!')
        #print('Esse triângulo é ESCALENO.')
    elif p==s==t:
        print('EQUILÁTERO!')
        #print('Esse triângulo é EQUILÁTERO.')
    else:
        print('ISÓSSELES!')
        #print('Esse triângulo é ISÓSSELES.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo.')