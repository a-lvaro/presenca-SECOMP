from sendEmail import sendEmail
from readData import ReadData


df = ReadData().link(
    'https://docs.google.com/spreadsheets/d/1Om1ZE9771rAQA27AyILw0sNSHZh10vqVwGGNhXaQ4ZA/edit?usp=sharing')

print(df)

# for i in range(df.shape[0]):
#     sendEmail(df['email'][i], df['nome'][i], df['cpf'][i])
