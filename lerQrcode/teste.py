import pandas as pd
from datetime import datetime

path = f'InscritosPresentes/workshopPython2022/presenca.csv'

df = pd.read_csv(path)
data = datetime.today().strftime('%Y-%m-%d')
print(df[df['data'] == data])
