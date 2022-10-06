import pandas as pd


class ReadData():

    def __saveSubrcribers(self, cpf: str, nome: str):
        with open('readQrcode/subscribers.txt', 'a') as f:
            data = f'{cpf}|{nome}'
            f.write(data + '\n')

    def link(self, link: str):

        fields = {'Endereço de e-mail': str, 'Nome completo': str, 'CPF': str}

        df = pd.read_csv(link[:-16] + 'export?format=csv',
                         usecols=fields, dtype=fields)

        df.rename(columns={'Endereço de e-mail': 'email',
                  'Nome completo': 'nome', 'CPF': 'cpf'},
                  inplace=True)

        df['cpf'] = df['cpf'].str.replace(r'\D', '', regex=True)

        for i in range(df.shape[0]):
            self.__saveSubrcribers(df['cpf'][i], df['nome'][i])

        return df
