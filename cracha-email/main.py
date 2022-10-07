from sendEmail import sendEmail
from readData import ReadData


df = ReadData().link(
    'https://docs.google.com/spreadsheets/d/1wXu_nNOkBjtcqxG6U4a-QEcmxCxslD9xTmNsf3WEsVg/edit?usp=sharing',
    save_subscribers=False)


for i in range(df.shape[0]):
    sendEmail(df['email'][i], df['nome'][i], df['cpf'][i],
              badge=False)
