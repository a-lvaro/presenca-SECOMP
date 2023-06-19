from lerQrcode.cameraQrCode import CameraQrCode
from os.path import exists

# aqui precisa de ^C para sair do programa
# precisa ser melhorado

def path(nomeEvento): 
    return f'InscritosPresentes/{nomeEvento}'

def menuCamera():
    print('\n\n\n' + '/\/' * 40)

    nomeEvento = '??'

    

    while not exists(path(nomeEvento)):
        nomeEvento = input('\n\n\tNome do evento: ')
        if not exists(path(nomeEvento)):
            print(f'\n\t\t\033[31mEvento não existe: {nomeEvento}\033[m')

    qrCode = CameraQrCode(nome_evento=nomeEvento)
    qrCode.inicializar()

    print('\n\n' + '/\/' * 40)
