from datetime import datetime
import pandas as pd
import os


class Presenca():
    def __init__(self, path: str):
        self.__data = lambda: datetime.today().strftime('%Y-%m-%d')
        self.__horario = lambda: datetime.today().strftime('%H-%M-%S')

        self.__path = path

        self.__fields = {'data': str, 'hora': str, 'cpf': str, 'nome': str}

    def __createFile(self, path: str) -> None:
        with open(path, 'w') as f:
            f.write('data,hora,cpf,nome\n')

    def getFile(self) -> pd.DataFrame:
        path = f'{self.__path}/presenca.csv'

        if not os.path.exists(path):
            self.__createFile(path)

        df = pd.read_csv(path, usecols=self.__fields, dtype=self.__fields)
        df['cpf'] = df['cpf'].astype(str)

        return df[df['data'] == self.__data()][['hora', 'nome', 'cpf']]

    def checarInscricao(self) -> dict:
        inscritos = {}

        with open(f'{self.__path}/inscritos.txt') as f:
            myDataList = f.read().splitlines()

        for data in myDataList:
            key, value = data.split('|')
            inscritos[key] = value

        return inscritos

    def salvarDados(self, cpf: str, nome: str) -> pd.DataFrame:
        with open(f'{self.__path}/presenca.csv', 'a') as p:
            p.write(self.__data() + ',' + self.__horario() +
                    ',' + cpf + ',' + nome + '\n')

        df = pd.read_csv(f'{self.__path}/presenca.csv',
                         usecols=self.__fields, dtype=self.__fields)

        return df[df['data'] == self.__data()][['hora', 'nome', 'cpf']]
