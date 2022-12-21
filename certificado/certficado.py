import pandas as pd
from numpy import NaN


class Certificado:
    def __init__(self, nome_evento: str, codigos: list, carga_horaria_aula: int):
        fields = {'data': str, 'hora': str, 'cpf': str, 'nome': str}
        path = f'InscritosPresentes/{nome_evento}/presenca.csv'

        self.__df = pd.read_csv(path, usecols=fields, dtype=fields)
        self.__datas = self.__df['data'].drop_duplicates().tolist()

        self.__setCodigoDias(codigos)
        self.__cargaHorariaFrequencia(self.__datas, carga_horaria_aula)
        self.__notaObtida()
        self.__formatar()
        self.__salvar(nome_evento)

    def __setCodigoDias(self, codigos: list):
        for data, codigo in zip(self.__datas, codigos):
            self.__df.loc[self.__df['data'] == data, [data]] = codigo

        # junta os cpfs iguais em apenas uma linha e coloca as presenças de todos os dias
        self.__df = self.__df.groupby(['nome', 'cpf'])[self.__datas].sum()

    def __cargaHorariaFrequencia(self, carga_horaria_aula) -> None:
        self.__df = self.__df[self.__datas].replace(0, NaN)

        carga_horaria_total = len(self.__datas) + carga_horaria_aula

        self.__df['carga horaria'] = (
            self.__df[self.__datas].count(axis=1) * carga_horaria_aula)
        self.__df['frequencia'] = (
            (self.__df['carga horaria'] / carga_horaria_total) * 100).round().astype('int')

    def __notaObtida(self) -> None:
        self.__df['nota'] = NaN

    def __formatar(self):
        ordem_colunas = ['carga horaria', 'nota', 'frequencia', 'codigo']

        self.__df[self.__datas] = self.__df[self.__datas].replace(NaN, '')
        self.__df['codigos'] = self.__df[self.__datas].apply("".join, axis=1)
        self.__df['codigos'].str[:-1]

        self.__df = self.__df.drop(self.__datas, axis='columns')
        self.__df = self.__df[ordem_colunas]

    def __salvar(self, nome_evento: str):
        path = f'InscritosPresentes/{nome_evento}/{nome_evento} PlanilhaDeBeneficiario.csv'
        with open(path, 'w') as f:
            f.write(
                'NOME PARTICIPANTE,NUMERO CPF,CARGA HORARIA,NOTA OBTIDA,FEQUÊNCIA,PARTICIPOU NO TEMA ?* (NOME TEMA TAL QUAL NO SISTEMA - SE HOUVER MAIS DE UM POR GENTIZLEZA SEPARE POR PONTO E VIRGULA)\n')


Certificado(nome_evento='workshopPython2022', codigos=[
                   '29172:', '29173'], carga_horaraia_total=4)
