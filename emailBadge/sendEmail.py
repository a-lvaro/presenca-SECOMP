import smtplib
from email.message import EmailMessage
from gerarCracha import GerarCracha


def sendEmail(i, reciver_email, name, cpf, badge=False):
    gmail_user = 'secomp@uem.br'
    gmail_password = '0b7c67f3'

    subject = 'Avaliação da SECOMP'
    content = f'''A SECOMP de 2022, chegou ao fim! 😔

Agradecemos a sua presença, {name}. Esperamos que você tenha gostado desse evento que foi preparado com muita dedicação pela organização ✨, e que as palestras tenham agregado conhecimento para a sua carreira! 

Vamos deixar aqui no e-mail um link para o formulário de avaliação do evento. Asim, podemos fazer uma SECOMP melhor ano que vem!
Link forms: https://forms.gle/Npk3JQMjH3pS7k5y5

NOS VEMOS ANO QUE VEM, NA VII SECOMP!🎉


Att,
Organização do evento'''

    newMessage = EmailMessage()
    newMessage['Subject'] = subject
    newMessage['From'] = gmail_user
    newMessage['To'] = reciver_email
    newMessage.set_content(content)

    if badge == True:
        GerarCracha().gerar(name, cpf)

        with open(f'emailBadge/crachasGeradosPDF/cracha{name}.pdf', 'rb') as f:
            file_data = f.read()
            file_name = f'cracha{name}.pdf'

        newMessage.add_attachment(
            file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.send_message(newMessage)

            print(f'{i}. e-mail sent to {name}')

    except Exception as ex:
        with open('emailNaoEnviado.csv', 'a') as f:
            f.write(reciver_email + ',' + name + '\n')

        print(f'{i}. Something went wrong…. {ex} {name}')
