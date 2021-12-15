print('='*20, 'DESAFIO 057-Validação de Dados', '='*20)

sexo = str(input('Informe o seu sexo: [F/M] ')).strip().upper()[0] #[0] só pega a primeira letra

while sexo not in 'FfmM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0].strip()
#enquanto o sexo nao for digitado dentro de 'FfMm', vai continuar perguntando.
print('Sexo {} registrado com sucesso.'.format(sexo))
