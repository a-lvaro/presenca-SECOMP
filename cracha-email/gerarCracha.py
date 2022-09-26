import qrcode
from PIL import Image, ImageDraw, ImageFont


class GerarCracha():
    def gerar(self, nome):
        self.cracha = Image.open('cracha-email/cracha recepcao.png')
        self.__setNomeCracha(nome)
        qrCode = self.__gerarQRcode(nome)
        self.__mergeImageQRcode(qrCode)

        self.cracha = self.cracha.convert("RGB")
        self.cracha.save(f"cracha-email/crachasGeradosPDF/cracha{nome}.pdf")

    def __setNomeCracha(self, nome):
        # font_type = ImageFont.truetype('Arial.ttf', 98)
        font_type = ImageFont.truetype(
            "cracha-email/keep_calm/KeepCalm-Medium.ttf", 98, encoding="unic")

        draw = ImageDraw.Draw(self.cracha)
        draw.text(xy=(200, 950), text=nome, fill=(
            255, 255, 255), font=font_type)

    def __gerarQRcode(self, nome):
        return qrcode.make(nome)

    def __mergeImageQRcode(self, qrCode):
        qrCode = qrCode.crop((35, 35, 335, 335))
        qrCode = qrCode.resize((600, 600))
        self.cracha.paste(qrCode, (470, 1220), mask=qrCode)
