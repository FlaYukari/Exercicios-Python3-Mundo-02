print('='*20, 'DESAFIO 059', '='*20)
import time

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

sair= False #escolha!=0
while sair is not True: # while escolha!=0:
    print('''      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa''')
    escolha= int(input('>>>>>Qual a sua opção? '))
    if escolha==1:
        print(f'A soma entre {valor1} + {valor2} é {valor1+valor2}.')
        print('=-='*10)
    elif escolha==2:
        print(f'A multiplicação entre {valor1} x {valor2} é {valor1*valor2}.')
        print('=-=' * 10)
    elif escolha == 3:
        lista=[valor1, valor2]
        print(f'O maior valor entre {valor1} e {valor2} é {max(lista)}.')
        print('=-=' * 10)
    elif escolha == 4:
        print('Informe os números novamente.')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif escolha == 5:
        sair = True
        print('Finalizando...')
        print('=-=' * 10)
        time.sleep(2)
    elif escolha > 5:
        print(f'Opção inválida. Tente novamente.')
        print('=-=' * 10)
print('Fim do programa! Volte sempre!')
