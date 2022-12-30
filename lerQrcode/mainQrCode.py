from lerQrcode.cameraQrCode import CameraQrCode

# aqui precisa de ^C para sair do programa
# precisa ser melhorado


def menu():
    print('\n\n\n' + '/\/' * 40)

    nomeEvento = input('\n\nNome do evento: ')

    qrCode = CameraQrCode(nome_evento=nomeEvento)
    qrCode.inicializar()

    print('\n\n' + '/\/' * 40)
