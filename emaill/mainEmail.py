import pandas as pd
from emaill.readData import ReadData
from emaill.enviarEmail import EnviarEmail


class MainEmail():
    def __init__(self):
        flag = True
        print('\n\n\n' + '+' * 100)
        print(
            '\033[31mÉ necessário conexão com a internet para executar essas opções \033[m')

        while flag:
            print('\n1. Enviar email com crachá do evento')
            print('2. Enviar um email informativo ou lembrete')
            print('3. Sair')

            opcao = input('Opcao: ')

            if opcao == '1':
                self.__emailCracha()

            elif opcao == '2':
                pass

            elif opcao == '3':
                flag = False

            else:
                print('\n\nOpção não encontrada')

        print('\n\n' + '+' * 100)

    def __emailCracha(self):
        print(
            '\n\n\033[33mPara gerar o crachá, é preciso colocá-lo na pasta cracha/arteCracha \033[m')
        print(
            '\033[33m     também é necessário que o seu crachá tenha exatamente o mesmo nome do evento \033[m')

        nome_evento = input('\nNome evento: ')
        link = input(
            'Link de acesso a planilha do Drive (deixar o acesso para qualquer um com o link): ')

        df = ReadData().link(link, nome_evento=nome_evento, registrar_inscricao=True)

        print(
            f'\n\033[35mArquivo lido \n    total de inscritos: {df.shape[0]}\033[m')

        path_arquivo_anexo = input(
            '\nCaso queira enviar um arquivo em anexo colocque o path, caso não, deixe em branco: ')
        if path_arquivo_anexo == '':
            path_arquivo_anexo = None

        print('\n\nEnviando e-mails')
        # enviar emails
        email = EnviarEmail()
        for i in range(df.shape[0]):
            email.enviar(i, df['email'][i], df['nome'][i], df['cpf'][i],
                         cracha=True,
                         path_arquivo_anexo=path_arquivo_anexo,
                         nome_evento=nome_evento)

        print('\n' + '+' * 30)
