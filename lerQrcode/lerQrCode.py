import cv2
import numpy as np
import pandas as pd
import os
from pyzbar.pyzbar import decode
from datetime import datetime
from somMario import SomMario
from presenca import Presenca


class LerQrCode():

    def __setFile(self, path: str) -> None:
        with open(path, 'w') as f:
            f.write('data,hora,cpf,nome\n')

    def __getFile(self, path: str):
        data = datetime.today().strftime('%Y-%m-%d')
        path = f'{path}/presenca.csv'

        if not os.path.exists(path):
            self.__setFile(path)

        df = pd.read_csv(path)
        df['cpf'] = df['cpf'].astype(str)

        return df[df['data'] == data][['hora', 'nome', 'cpf']]

    def __checarInscricao(self, path: str):
        inscritos = {}

        with open(f'{path}/inscritos.txt') as f:
            myDataList = f.read().splitlines()

        for data in myDataList:
            key, value = data.split('|')
            inscritos[key] = value

        return inscritos

    def __saveData(self, path, cpf, nome):

        data = datetime.today().strftime('%Y-%m-%d')
        hora = datetime.today().strftime('%H-%M-%S')

        with open(f'{path}/presenca.csv', 'a') as p:
            p.write(data + ',' + hora + ',' + cpf + ',' + nome + '\n')

        df = pd.read_csv(f'{path}/presenca.csv')
        df['cpf'] = df['cpf'].astype(str)

        return df[df['data'] == data][['hora', 'nome', 'cpf']]

    def camera(self, nome_evento: str):
        mario = SomMario()
        presenca = Presenca()

        path = f'InscritosPresentes/{nome_evento}'

        df_presenca = self.__getFile(path)
        # pegar lista de inscritos no evento
        inscritos = self.__checarInscricao(path)

        cap = cv2.VideoCapture(0)
        cap.set(3, 940)
        cap.set(4, 780)

        while True:

            _, img = cap.read()

            for barcode in decode(img):
                qrCodeCPF = barcode.data.decode(
                    'utf-8').encode('shift-jis').decode('utf-8')

                if qrCodeCPF in inscritos.keys():        # match CPF
                    qrcodeColor = (0, 255, 0)
                    mario.tocar('inscrito')

                    if qrCodeCPF not in df_presenca['cpf'].tolist():
                        df_presenca = self.__saveData(path, qrCodeCPF,
                                                      inscritos[qrCodeCPF])

                    else:
                        horas = df_presenca[df_presenca['cpf']
                                            == qrCodeCPF]['hora'].tolist()

                        if max(horas)[:2] != datetime.today().strftime('%H'):
                            df_presenca = self.__saveData(
                                path, qrCodeCPF, inscritos[qrCodeCPF])

                else:
                    qrcodeColor = (0, 0, 255)
                    mario.tocar('naoInscrito')

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, qrcodeColor, 5)
                pts2 = barcode.rect

                if qrcodeColor == (0, 0, 255):
                    nome = 'nao inscrito no workshop'
                else:
                    nome = inscritos[qrCodeCPF]

                cv2.putText(img, nome, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, qrcodeColor, 2)

            img = cv2.flip(img, 1)
            cv2.imshow('Result', img)
            cv2.waitKey(1)


camera = LerQrCode()
camera.camera('workshopPython2022')
