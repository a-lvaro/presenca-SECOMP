import pandas as pd

from enviarEmail import enviarEmail
from gerarCracha import GerarCracha

# df = pd.read_csv(
#     'https://docs.google.com/spreadsheets/d/1BeHwzZdDUOSDaKCSG5drdh2mVoUSvRwEeTbNKqZFQrM/export?format=csv')

df = pd.DataFrame({'e-mail': ['ra120113@uem.br', 'aaflneto@hotmail.com'],
                   'nome': ['Álvaro de Araújo Ferreira Lima Neto Reis da Silva', 'Álvaro']})


cracha = GerarCracha()
df['nome'].apply(GerarCracha().gerar)


# # df['cracha'][0].show()


# for i in range(df.shape[0]):
#     enviarEmail(df['e-mail'][i], df['nome'][i])
