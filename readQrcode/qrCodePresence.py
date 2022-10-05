import cv2
import numpy as np
import os.path
from pyzbar.pyzbar import decode
from datetime import datetime, date
from playsound import playsound
from threading import Thread


class QrCodePresence():

    def __openFile(self):
        time = datetime.now()

        if time.hour < 12:
            file = f'readQrcode/presence/workshopLatex{date.today()}.csv'
        elif time.hour < 15:
            file = f'readQrcode/presence/mesaredonda{date.today()}.csv'
        else:
            file = f'readQrcode/presence/feiradeOportunidades{date.today()}.csv'

        with open(file, 'a'):
            pass

        return np.loadtxt(file, delimiter=",", dtype=str, usecols=(0)), file

    def __checkSubscribers(self):
        subscribers = {}

        with open('readQrcode/subscribers.txt') as f:
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

        return np.loadtxt(file, delimiter=",", dtype=str, usecols=(0))

    def __sound(sef, sound):
        playsound(f'readQrcode/marioSounds/{sound}.mp3')

    def camera(self):

        # não vai tocar pq não tem start
        sound = Thread(target=self.__sound, args=('marioTheme',))

        presenceList, file = self.__openFile()
        subscribers = self.__checkSubscribers()

        cap = cv2.VideoCapture(0)
        cap.set(3, 940)
        cap.set(4, 780)

        while True:

            time = datetime.now()
            if time.hour > 17 and not os.path.exists(f'readQrcode/presence/presencaAposIntervalo{date.today()}.csv'):
                presenceList, file = self.__openFile()

            _, img = cap.read()

            for barcode in decode(img):
                qrcodeData = barcode.data.decode(
                    'utf-8').encode('shift-jis').decode('utf-8')

                if qrcodeData in subscribers.keys():        # match CPF
                    qrcodeColor = (0, 255, 0)

                    if qrcodeData not in presenceList:
                        presenceList = self.__saveData(file, qrcodeData,
                                                       subscribers[qrcodeData])

                    if sound.is_alive() == False:
                        sound = Thread(target=self.__sound, args=('coin',))
                        sound.start()

                else:
                    qrcodeColor = (0, 0, 255)

                    if sound.is_alive() == False:
                        sound = Thread(target=self.__sound, args=('deth',))
                        sound.start()

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
