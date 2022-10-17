from sendEmail import sendEmail
from readData import ReadData


df = ReadData().link(
    'link',
    save_subscribers=False)

print(df)

for i in range(df.shape[0]):
    sendEmail(i, df['email'][i], df['nome'][i], df['cpf'][i],
              badge=False)
