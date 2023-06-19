import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageColor

# https://gist.github.com/Eyongkevin/adbac2334f1355d8045111c264d80621


class GerarCracha():
    def gerar(self, nome: str, cpf: str, nome_evento: str):
        self.cracha = Image.open(f'cracha/arteCracha/cracha {nome_evento}.png')
        self.__setNomeCracha(nome)
        qrCode = self.__gerarQRcode(cpf)
        self.__mergeImageQRcode(qrCode)

        self.cracha = self.cracha.convert("RGB")
        self.cracha.save(f"cracha/crachasGeradosPDF/cracha{nome}.pdf")

    def __setNomeCracha(self, nome: str):
        # font_type = ImageFont.truetype('Arial.ttf', 98)
        font_type = ImageFont.truetype(
            "cracha/fonte/vt323/VT323-Regular.ttf", 90, encoding="unic")

        # sanitize o nome Deixando-o Na Forma de Título
        nome = nome.strip().title().replace(" De ", " de ")

        draw = ImageDraw.Draw(self.cracha)
        fill_color = ImageColor.getrgb('#ff61c6')
        draw.text(xy=(671, 1650), text=self.__wrapText(nome, font_type, 1320), fill=fill_color,
                font=font_type,
            align="center", spacing=32, anchor="mm")

        # 681, 900
        # 681, 1000
        # 681, 1500
        # 681, 1800
        # 681, 1650
        # 671, 1650

    def __gerarQRcode(self, cpf):
        qr = qrcode.QRCode(border=1)
        qr.add_data(cpf)
        return qr.make_image()

    def __mergeImageQRcode(self, qrCode):
        qrCode = qrCode.resize((490, 490))
        self.cracha.paste(qrCode, (405, 965), mask=qrCode)
        # 453, 1047
        # 440, 1000
        # 430, 990
        # 420, 980
        # 400, 960
        # 405, 965


    def __wrapText(self, text, font, maxwidth):
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
