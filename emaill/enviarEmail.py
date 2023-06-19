import smtplib, ssl
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
        subject = f'Prezado {nome} do Curso de Ciência da Computação ou Informática,'
        content = f'''Gostaríamos de te parabenizar pela aprovação no vestibular da UEM e pelo ingresso nos cursos de Ciência da Computação/Informática! Sejam muito bem vindos(as) à UEM!

O PET-Informática, o Centro Acadêmico de Ciência da Computação (CACCOM), o Centro Acadêmico de  Informática (CAINFO), o grupo Conectadas e os professores do Departamento de Informática (DIN) estão organizando a Semana de Recepção aos Calouros, na qual ocorrerão palestras, apresentações e integrações!

O evento será realizado no DIN (bloco C-56), nos dias 28/06, 29/06 e 30/06, nos horários listados na imagem abaixo. Nesses dias as aulas estarão dispensadas.

Pedimos para que compareçam e participem das atividades. É um evento muito importante para que vocês se situem no ambiente universitário da UEM e conheçam seus colegas.

Acessem o site da recepção dos calouros para mais informações.

http://din.uem.br/recepcaocalouros/

Abraços,
Equipe do DIN.
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