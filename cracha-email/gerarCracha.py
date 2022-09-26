import qrcode
from PIL import Image, ImageDraw, ImageFont

# https://gist.github.com/Eyongkevin/adbac2334f1355d8045111c264d80621


def wrapText(text, font, maxwidth):
    lines = []
    if font.getsize(text)[0] <= maxwidth:
        lines.append(text)
    else:
        words = text.split()
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= maxwidth:
                line += words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line.strip())
    return '\n'.join(lines)


class GerarCracha():
    def gerar(self, nome):
        self.cracha = Image.open('cracha-email/cracha recepcao.png')
        self.__setNomeCracha(nome)
        qrCode = self.__gerarQRcode(nome)
        self.__mergeImageQRcode(qrCode)

        self.cracha = self.cracha.convert("RGB")
        self.cracha.save(f"cracha-email/crachasGeradosPDF/cracha{nome}.pdf")

    def __setNomeCracha(self, nome: str):
        # font_type = ImageFont.truetype('Arial.ttf', 98)
        font_type = ImageFont.truetype(
            "cracha-email/keep_calm/KeepCalm-Medium.ttf", 110, encoding="unic")

        # sanitize o nome Deixando-o Na Forma de Título
        nome = nome.strip().title().replace(" De ", " de ")

        draw = ImageDraw.Draw(self.cracha)
        draw.text(xy=(781, 980), text=wrapText(nome, font_type, 1320), fill=(
            255, 255, 255), font=font_type,
            align="center", spacing=32, anchor="mm")

    def __gerarQRcode(self, nome):
        qr = qrcode.QRCode(border=2)
        qr.add_data(nome)
        return qr.make_image()

    def __mergeImageQRcode(self, qrCode):
        # qrCode = qrCode.crop((35, 35, 335, 335))
        qrCode = qrCode.resize((505, 505))
        self.cracha.paste(qrCode, (526, 1242), mask=qrCode)
