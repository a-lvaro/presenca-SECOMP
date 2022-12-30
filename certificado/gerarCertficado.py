import pandas as pd
from numpy import NaN


class Certificado:
    def __init__(self, nome_evento: str, carga_horaria_aula: int):
        fields = {'data': str, 'hora': str, 'cpf': str, 'nome': str}
        path = f'InscritosPresentes/{nome_evento}/presenca.csv'

        self._cargaHorariaArula = carga_horaria_aula
        self.__nomeEvento = nome_evento

        self.__df = pd.read_csv(path, usecols=fields, dtype=fields)
        self.datas = self.__df['data'].drop_duplicates().tolist()

    def quantasAulas(self) -> int:
        return len(self.datas)

    def gerar(self, codigos: list):
        self.__setCodigoDias(codigos)
        self.__cargaHorariaFrequencia(self._cargaHorariaArula)
        self.__notaObtida()
        self.__formatar()
        self.__salvar(self.__nomeEvento)

    def __setCodigoDias(self, codigos: list):
        for data, codigo in zip(self.datas, codigos):
            self.__df.loc[self.__df['data'] == data, [data]] = f'{codigo};'

        # junta os cpfs iguais em apenas uma linha e coloca as presenças de todos os dias
        self.__df = self.__df.groupby(['nome', 'cpf'])[self.datas].sum()

    def __cargaHorariaFrequencia(self, carga_horaria_aula) -> None:
        self.__df = self.__df[self.datas].replace(0, NaN)

        carga_horaria_total = len(self.datas) * carga_horaria_aula

        self.__df['carga horaria'] = (
            self.__df[self.datas].count(axis=1) * carga_horaria_aula)
        self.__df['frequencia'] = (
            (self.__df['carga horaria'] / carga_horaria_total) * 100).round().astype('int')

    def __notaObtida(self) -> None:
        self.__df['nota'] = NaN

    def __formatar(self):
        ordem_colunas = ['carga horaria', 'nota', 'frequencia', 'codigos']

        self.__df[self.datas] = self.__df[self.datas].replace(NaN, '')
        self.__df['codigos'] = self.__df[self.datas].apply("".join, axis=1)
        self.__df['codigos'] = self.__df['codigos'].str[:-1]

        self.__df = self.__df.drop(self.datas, axis='columns')
        self.__df = self.__df[ordem_colunas]
        self.__df.rename(columns={'carga horaria': 'CARGA HORARIA', 'nota': 'NOTA OBTIDA', 'frequencia': 'FREQUÊNCIA',
                         'codigos': 'PARTICIPOU NO TEMA ?* (NOME TEMA TAL QUAL NO SISTEMA - SE HOUVER MAIS DE UM POR GENTIZLEZA SEPARE POR PONTO E VIRGULA)'}, inplace=True)
        self.__df.index.names = ['NOME PARTICIPANTE', 'NUMERO CPF']

    def __salvar(self, nome_evento: str):
        path = f'InscritosPresentes/{nome_evento}/{nome_evento} PlanilhaDeBeneficiario.xlsx'
        self.__df.to_excel(path)

        print('\n\n' + '-' * 110 + '\n')
        print(f'certicifados na pasta {path}')
        print('\n' + '-' * 110)
