import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime, date


class QrCodePresence():

    def __openFile(self):
        time = datetime.now()

        if time.hour < 18:
            file = f'presenca/presenca{date.today()}.csv'
        else:
            file = f'presenca/presencaAposIntervalo{date.today()}.csv'

        with open(file, 'a'):
            pass

        return np.loadtxt(file, delimiter=",", dtype=str, usecols=(0)), file

        # if time.hour == 13 and time.day == 4:
        #     file = f'presenca/presencaWorshopEleflow{date.today()}.csv'
        # elif time.hour == 13 and time.day == 6:  # aqui vão acontecer dois workshops
        #     file = f'presenca/presencaWorshopEleflow{date.today()}.csv'
        # elif time.hour == 13 and time.day == 7:
        #     file = f'presenca/presencaWorshopFusca{date.today()}.csv'

    def __checkSubscribers(self):
        subscribers = {}

        with open('presenca/subscribers.txt') as f:
            myDataList = f.read().splitlines()

        for data in myDataList:
            key, value = data.split('|')
            subscribers[key] = value

        return subscribers

    def __saveData(self, file, cpf, nome):
        time = datetime.now()

        with open(file, 'a') as p:
            p.write(cpf + ',' + nome + ',')
            p.write(f'{time.hour}:{time.minute}:{time.second}\n')

        if time.hour >= 18:
            file = f'presenca/presencaAposIntervalo{date.today()}.csv'

            with open(file, 'a'):
                pass

        return np.loadtxt(file, delimiter=",", dtype=str, usecols=(0)), file

    def camera(self):

        presenceList, file = self.__openFile()
        subscribers = self.__checkSubscribers()

        cap = cv2.VideoCapture(0)
        cap.set(3, 940)
        cap.set(4, 780)

        while True:

            _, img = cap.read()

            for barcode in decode(img):
                qrcodeData = barcode.data.decode(
                    'utf-8').encode('shift-jis').decode('utf-8')

                if qrcodeData in subscribers.keys():        # match CPF
                    qrcodeColor = (0, 255, 0)

                    if qrcodeData not in presenceList:
                        presenceList, file = self.__saveData(file, qrcodeData,
                                                             subscribers[qrcodeData])

                else:
                    qrcodeColor = (0, 0, 255)

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, qrcodeColor, 5)
                pts2 = barcode.rect

                if qrcodeColor == (0, 0, 255):
                    nome = 'nao inscrito na SECOMP'
                else:
                    nome = subscribers[qrcodeData]

                cv2.putText(img, nome, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, qrcodeColor, 2)

            img = cv2.flip(img, 1)
            cv2.imshow('Result', img)
            cv2.waitKey(1)


QrCodePresence().camera()
