
import pandas as pd


def importData(link: str):

    fields = {'Endereço de e-mail': str, 'Nome completo': str, 'CPF': str}

    df = pd.read_csv(link[:-16] + 'export?format=csv',
                     usecols=fields, dtype=fields)

    df.rename(columns={'Endereço de e-mail': 'email',
                       'Nome completo': 'nome', 'CPF': 'cpf'},
              inplace=True)

    df['cpf'] = df['cpf'].str.replace(r'\D', '', regex=True)

    return df


links = {'SECOMP': 'https://docs.google. com/spreadsheets/d/1MEqYORuZvMLv7qObalqSclSWGjnGDNTkbrCwsjr6SmQ/edit?usp=sharing',  # inscrição SECOMP
         # worshop eleflow turma 1
         'workshop eleflow 01': 'https://docs.google.com/spreadsheets/d/17idvt9JD8QZYwKKK9KydhCTRB5QmDw4fQccyBlJxBNE/edit?usp=sharing',
         # Workshop Eleflow turma 2
         'workshop eleflow 02': 'https://docs.google.com/spreadsheets/d/1D9Fn6POWleAWzPCdQVvLNF-_F1fIGLD9USjsBmJ39X8/edit?usp=sharing',
         # Workshop Latex
         'workshop latex': 'https://docs.google.com/spreadsheets/d/14vzi7EFahgoZpaylB9VXJVhz2K8nAt0QjVK7tfLfA68/edit?usp=sharing',
         # Workshop pygames
         'workshop pygames': 'https://docs.google.com/spreadsheets/d/1wXu_nNOkBjtcqxG6U4a-QEcmxCxslD9xTmNsf3WEsVg/edit?usp=sharing',
         # Workshop Fusca turma 1
         'workshop fusca 01': 'https://docs.google.com/spreadsheets/d/1hf-gr08PakzbZpWVHscN9lb4zcZ4UZJ2cFkPEOvqyFY/edit?usp=sharing',
         # Workshop Fusca turma 2
         'workshop fusca 02': 'https://docs.google.com/spreadsheets/d/14J7dYVXuGuPjFCo_grYPy_ULR9iXklVg0_ScEAHl91I/edit?usp=sharing'}


df_registeredEvent = importData(list(links.values())[0])

for link in links.values():
    df_registerEvent = pd.merge(
        df_registeredEvent, importData(link), how='outer', on='cpf')

print("Total de pessoas inscritas no evento: ", df_registeredEvent.shape[0])
print(df_registeredEvent.shape)
