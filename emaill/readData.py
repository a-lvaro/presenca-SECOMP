import pandas as pd
import os


class ReadData():

    def __salvarInscritos(self, cpf: str, nome: str, nome_evento: str):
        if os.path.exists(f'InscritosPresentes/{nome_evento}') == False:
            os.makedirs(f'InscritosPresentes/{nome_evento}')

        with open(f'InscritosPresentes/{nome_evento}/inscritos.txt', 'a') as f:
            data = f'{cpf}|{nome}'
            f.write(data + '\n')

    def link(self, link: str, nome_evento=None, registrar_inscricao=False):

        fields = {'Endereço de e-mail': str, 'Nome completo': str, 'CPF': str}

        df = pd.read_csv(link[:-16] + 'export?format=csv',
                         usecols=fields, dtype=fields)

        df.rename(columns={'Endereço de e-mail': 'email',
                  'Nome completo': 'nome', 'CPF': 'cpf'},
                  inplace=True)

        df.dropna(how='all', inplace=True)

        df['cpf'] = df['cpf'].str.replace(r'\D', '', regex=True)

        if registrar_inscricao == True:
            for i in range(df.shape[0]):
                self.__salvarInscritos(
                    df['cpf'][i], df['nome'][i], nome_evento)

        return df
