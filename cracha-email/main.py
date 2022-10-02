from sendEmail import sendEmail
from readData import ReadData


df = ReadData().link(
    'https://docs.google.com/spreadsheets/d/1b5rVn-izT9YbOotsbaCrxNR_wwvjxrvTlO2E5UPrdi8/edit?usp=sharing')


for i in range(df.shape[0]):
    sendEmail(df['email'][i], df['nome'][i], df['cpf'][i])
