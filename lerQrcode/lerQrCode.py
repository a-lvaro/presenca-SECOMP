import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime
from somMario import SomMario
from presenca import Presenca


class LerQrCode():
    def __init__(self, nome_evento: str):
        path = f'InscritosPresentes/{nome_evento}'

        self.__mario = SomMario()
        self.__presenca = Presenca(path)

        self.__data = lambda: datetime.today().strftime('%Y-%m-%d')
        self.__horario = lambda: datetime.today().strftime('%H-%M-%S')

    def __inicializarCamera(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 940)
        cap.set(4, 780)

        return cap

    def __molduraQrCode(self, img, barcode, qrcodeColor: tuple, nome: str) -> None:
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, qrcodeColor, 5)
        pts2 = barcode.rect

        cv2.putText(img, nome, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, qrcodeColor, 2)

    def camera(self) -> None:
        df_presenca = self.__presenca.getFile()
        inscritos = self.__presenca.checarInscricao()

        verde = (0, 255, 0)
        vermelho = (0, 0, 255)

        cap = self.__inicializarCamera()

        while True:
            _, img = cap.read()

            for barcode in decode(img):
                qrCodeCPF = barcode.data.decode(
                    'utf-8').encode('shift-jis').decode('utf-8')

                if qrCodeCPF in inscritos.keys():        # match CPF
                    qrcodeColor = verde
                    nome = inscritos[qrCodeCPF]
                    self.__mario.tocar('inscrito')

                    if qrCodeCPF not in df_presenca['cpf'].tolist():
                        df_presenca = self.__presenca.salvarDados(
                            qrCodeCPF, inscritos[qrCodeCPF])

                    else:
                        horas = df_presenca[df_presenca['cpf']
                                            == qrCodeCPF]['hora'].tolist()

                        if max(horas)[:2] != datetime.today().strftime('%H'):
                            df_presenca = self.__presenca.salvarDados(
                                qrCodeCPF, inscritos[qrCodeCPF])

                else:
                    qrcodeColor = vermelho
                    nome = 'nao inscrito no workshop'
                    self.__mario.tocar('naoInscrito')

                self.__molduraQrCode(img, barcode, qrcodeColor, nome)

            img = cv2.flip(img, 1)
            cv2.imshow('Result', img)
            cv2.waitKey(1)


camera = LerQrCode('workshopPython2022')
camera.camera()
