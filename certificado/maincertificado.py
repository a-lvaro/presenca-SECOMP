from certificado.gerarCertficado import Certificado
from os.path import exists


def menuCertificado():
    print('\n\n\n' + '/\/' * 40)
    nomeEvento = ''
    codigos = ''

    def path(
        nomeEvento): return f'InscritosPresentes/{nomeEvento}/presenca.csv'

    while not exists(path(nomeEvento)):
        nomeEvento = input('\n\n\tNome do evento: ')
        if not exists(path(nomeEvento)):
            print(f'\n\t\t\033[31mEvento não existe: {nomeEvento}\033[m')

    cargaHorariaAula = int(input('\tCarga horaria por aula: '))

    certificado = Certificado(nome_evento=nomeEvento,
                              carga_horaria_aula=cargaHorariaAula)

    print(
        f'\n\n\033[32mSão necessários {certificado.quantasAulas()} códigos para os dias {certificado.datas}\033[m')
    print(
        f'\033[32mCarga horária total do evento é de {cargaHorariaAula * certificado.quantasAulas()} horas\033[m\n')

    while len(codigos) != certificado.quantasAulas():
        codigos = input('\n\tCódigos (separá-los por vírgula): ').split(',')
        codigos = [i.strip() for i in codigos]

        if len(codigos) != certificado.quantasAulas():
            print(
                f'\n\t\033[31mÉ necessário ter {certificado.quantasAulas()} códigos\033[m')

    certificado.gerar(codigos)

    print('\n\n' + '/\/' * 40)
