import smtplib
from email.message import EmailMessage


def enviarEmail(reciver_email, nome):
    gmail_user = 'secomp@uem.br'
    gmail_password = '0b7c67f3'

    subject = 'Crachá virtual VI SECOMP'
    content = '''Você se inscreveu para a SECOMP 2022, o melhor evento de tecnologia da cidade!

Agora, prepare-se para embarcar nessa jornada incrível que preparamos para você.

Para começar, guarde este e-mail pois nele anexamos o seu crachá virtual com um QR code que irá contabilizar a sua presença no evento. É de grande importância que você apresente esse crachá no dia, para garantir sua AAC, caso necessite. 
Anote a data das atividades que você se inscreveu e aguarde até o grande dia!

Agradecemos a sua participação e esperamos te ver lá. :)

Fique atento às nossas redes sociais para possíveis mudanças!

Em caso de dúvida e para se atualizar sobre as novidades da SECOMP, acesse:
       → Site: https://www.din.uem.br/secomp/
       → Instagram: https://www.instagram.com/p/CiEFHH3sARM/
       → Linketree: https://linktr.ee/secompuem
       → Discord: https://discord.gg/P87bV3xz9M
       → Twitch: https://www.twitch.tv/secompuem'''

    newMessage = EmailMessage()
    newMessage['Subject'] = subject
    newMessage['From'] = gmail_user
    newMessage['To'] = reciver_email
    newMessage.set_content(content)

    with open(f'cracha-email/crachasGeradosPDF/cracha{nome}.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    newMessage.add_attachment(
        file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.send_message(newMessage)

            print(f'e-mail sent to {nome}')

    except Exception as ex:
        with open('emailNaoEnviado.csv', 'a') as f:
            f.write(reciver_email + ',' + nome + '\n')

        print("Something went wrong….", ex, nome)
