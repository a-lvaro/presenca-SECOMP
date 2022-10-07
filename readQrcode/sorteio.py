from random import shuffle
import numpy as np

file = 'presenca2022-10-06.csv'
lista = np.loadtxt(file, delimiter=",", dtype=str, usecols=(1))

shuffle(lista)

for sorteado in lista:
    print(sorteado)
    input()
