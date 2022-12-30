from certificado.gerarCertficado import Certificado


def menuCertificado():
    print('\n\n\n' + '/\/' * 40)

    nomeEvento = input('\n\nNome do evento: ')
    codigos = input(
        'Códigos (separá-los por vírgula e por orgem cronológica): ')
    cargaHorariaAula = input('Qual a carga horaria por aula: ')

    certificado = Certificado()

    print('\n\n' + '/\/' * 40)
