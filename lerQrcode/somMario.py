from playsound import playsound
from threading import Thread

class SomMario():
    def __init__(self):
        # não vai tocar pq não tem start
        self.musica = Thread(target=self.__sound, args=('marioTheme',))

    def __sound(self, sound):
        playsound(f'lerQrcode/marioSounds/{sound}.mp3')

    def tocar(self, estado :str):
        if self.musica.is_alive() == False:
            if estado == 'inscrito':
                self.musica = Thread(target=self.__sound, args=('coin',))
                self.musica.start()

            elif estado == 'naoInscrito':
                self.musica = Thread(target=self.__sound, args=('deth',))
                self.musica.start()
    
    