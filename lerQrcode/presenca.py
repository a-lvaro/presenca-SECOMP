from datetime import datetime
import pandas as pd
import os

class Presenca():
    def __setFile(self, path: str) -> None:
        with open(path, 'w') as f:
            f.write('data,hora,cpf,nome\n')

    def __getFile(self, path :str):
        data = datetime.today().strftime('%Y-%m-%d')
        path = f'{path}/presenca{data}.csv'
        
        if not os.path.exists(path):
            self.__setFile(path)

        df = pd.read_csv(path)
        df['cpf'] = df['cpf'].astype(str)