# se o nome da pasta for 'email' o python vai importar uma biblioteca própria
from emaill.mainEmail import MainEmail
from lerQrcode.mainQrCode import menuCamera
from certificado.maincertificado import menuCertificado

flag = True
while flag:
    print('\n\n' + '*' * 100)
    print('\n1. Criar novo evento / enviar email')
    print('2. Ler as presenças por meio do QrCode')
    print('3. Gerar certificados')
    print('4. Sair')

    opcao = input('\nOpção: ')
    # 0qvdd0Lw1JKF3lnRw6QU
    # pet@din.uem.br

    print('*' * 100)

    if opcao == '1':
        MainEmail()

    elif opcao == '2':
        menuCamera()

    elif opcao == '3':
        menuCertificado()

    elif opcao == '4':
        flag = False

    else:
        print('\n\nOpção não encontrada')
