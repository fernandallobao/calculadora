#Crie uma calculadora que faça as 4 operações básicas da matemática, e ao final, pergunte ao usuário se deseja fazer outro cálculo ou se deseja encerrar o programa. Ao terminar, envio o arquivo .py.

print(f'{'-'*10} Olá bem vindo a calculadora! {'-'*10}')
while True:
    
    print(f'{'-'*10} OPERAÇÕES {'-'*10}')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')

    op = int(input('Selecione uma operação: '))
    x = int(input('Informe o primeiro numero para a operação: '))
    y = int(input('Informe o segundo numero para a operação: '))

    match op:
        case 1:
            operacao = x + y
            print(operacao)
        case 2:
            operacao = x - y
            print(operacao)
        case 3:
            operacao = x * y
            print(operacao)
        case 4:
            operacao = x / y
            print(operacao)

    
    continuar = input('Deseja continuar (s/n)?').lower()
    if continuar == 's':
        continue
    else:
        break
print('Programa encerrado!')