import pandas as pd

from enviarEmail import enviarEmail
from gerarCracha import GerarCracha


def teste(cpf, nome):
    with open('nomeTeste.txt', 'a') as f:
        data = f'{cpf}|{nome}'
        f.write(data + '\n')


# df = pd.read_csv(
#     'https://docs.google.com/spreadsheets/d/1BeHwzZdDUOSDaKCSG5drdh2mVoUSvRwEeTbNKqZFQrM/export?format=csv')

df = pd.DataFrame({'e-mail': ['ra120113@uem.br', 'aaflneto@hotmail.com'],
                   'nome': ['Álvaro de Araújo Ferreira Lima Neto Reis da Silva', 'Álvaro'],
                   'cpf': ['09934465877', '78846627344']})

print(df)
print("\n\n\n")

for i in range(df.shape[0]):
    teste(df['cpf'][i], df['nome'][i])

# for i in range(df.shape[0]):
#     enviarEmail(df['e-mail'][i], df['nome'][i], df['cpf'][i])
