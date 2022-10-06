from sendEmail import sendEmail
from readData import ReadData


df = ReadData().link(
    'https://docs.google.com/spreadsheets/d/1_KHjLxX2K2zMoUjT_n6vfoUMARLYnBO684AZm3Z-beE/edit?usp=sharing')


for i in range(df.shape[0]):
    sendEmail(df['email'][i], df['nome'][i], df['cpf'][i], badge=True)
