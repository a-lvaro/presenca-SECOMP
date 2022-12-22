# se o nome da pasta for 'email' o python vai importar uma biblioteca própria
from emaill.mainEmail import MainEmail

flag = True
while flag:
    print('\n\n' + '*' * 100)
    print('\n1. Criar novo evento / enviar email')
    print('2. Ler as presenças por meio do QrCode')
    print('3. Fazer arquivo dos certificados')
    print('4. Sair')

    opcao = input('\nOpção: ')

    print('*' * 100)

    if opcao == '1':
        MainEmail()

    elif opcao == '2':
        pass

    elif opcao == '3':
        pass

    elif opcao == '4':
        flag = False

    else:
        print('\n\nOpção não encontrada')
