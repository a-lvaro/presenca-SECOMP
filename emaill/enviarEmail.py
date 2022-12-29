import smtplib
from email.message import EmailMessage
from cracha.gerarCracha import GerarCracha


class EnviarEmail():
    def __init__(self, gmail_user: str, senha: str, cracha=False, path_arquivo_anexo=None, nome_evento=None):
        self.__gmail_user = gmail_user
        self.__gmail_password = senha

        self.__cracha = cracha
        self.__pathArquivoAnexo = path_arquivo_anexo
        self.__nomeEvento = nome_evento


    def enviar(self, contador: int, reciver_email: str, nome: str, cpf: str):

        self.__newMessage = EmailMessage()

        subject, content = self.__corpoEmail(nome)

        self.__newMessage['Subject'] = subject
        self.__newMessage['From'] = self.__gmail_user
        self.__newMessage['To'] = reciver_email
        self.__newMessage.set_content(content)

        # se o anexo vir antes irá ocorrer erro
        self.__anexoCracha(nome=nome, cpf=cpf,
                           path_arquivo=self.__pathArquivoAnexo,
                           nome_evento=self.__nomeEvento)

        self.__enviarEmail(contador, reciver_email, nome)

    def __corpoEmail(self, nome: str) -> str and str:
        subject = 'Workshop Python PET-Informática'
        content = f'''Olá {nome}!

Muito obrigado pela sua inscrição no Workshop de Python do PET-Informática! Só relembrando, teremos aulas nos dias 10/12 (amanhã!) e 17/12, sempre das 8:30 às 11:30, no bloco C56.

Neste e-mail, enviamos em anexo seu crachá virtual. É pelo QR Code do seu crachá que a presença será contabilizada. Você precisará escanear seu QR code ao chegar na aula e ao sair dela, então faça download dele no seu celular. Toleramos atrasos de 30 minutos no máximo, mais do que isso não será contabilizada presença.

Para quem ainda não entrou no Google Classroom, peço que entrem na seguinte sala com o seu e-mail pessoal. É por esta sala que disponibilizaremos os materiais e listas de exercícios para serem feitas em casa. Após cada aula, vamos liberar exercícios que representarão 1/4 da carga horária do Workshop, ou seja, 1 hora cada lista de exercícios, totalizando 3 horas. As listas deverão ser  entregues para receber a carga horária total do Workshop.
Classroom: https://classroom.google.com/c/NTQwMDk3MTk2MjUz?cjc=4gzse6x

Por fim, para os que irão utilizar o computador próprio e ainda não possuem o Python 3 instalado, pedimos que já venham com ele instalado em sua máquina(https://www.python.org/downloads/). Podem utilizar qualquer IDE para programar, mas recomendamos o VSCode (https://code.visualstudio.com/download) ou o PyCharm (https://www.jetbrains.com/pycharm/download/#section=windows).

Mais uma vez, obrigado por sua inscrição e nos vemos nas aulas!

Att,
PET-Informática

'''
        return subject, content

    def __anexoCracha(self, nome: str, cpf: str, path_arquivo: str, nome_evento: str) -> None:

        if self.__cracha == True:
            GerarCracha().gerar(nome, cpf, nome_evento)

            with open(f'cracha/crachasGeradosPDF/cracha{nome}.pdf', 'rb') as f:
                file_data = f.read()
                file_name = f'cracha{nome}.pdf'

            self.__newMessage.add_attachment(
                file_data, maintype='application', subtype='octet-stream', filename=file_name)

        if path_arquivo != None:
            with open(path_arquivo, 'rb') as f:
                file_data = f.read()
                file_name = path_arquivo.split('/')[-1]

            self.__newMessage.add_attachment(
                file_data, maintype='application', subtype='octet-stream', filename=file_name)

    def __enviarEmail(self, contador: int, reciver_email: str, nome: str) -> None:
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.__gmail_user, self.__gmail_password)
                smtp.send_message(self.__newMessage)

                print(f'{contador + 1}. e-mail sent to {nome}')

        except Exception as ex:
            with open(f'InscritosPresentes/{self.__nomeEvento}/emailNaoEnviado.csv', 'a') as f:
                f.write(reciver_email + ',' + nome + '\n')

            print(f'{contador + 1}. Something went wrong…. {ex} {nome}')
