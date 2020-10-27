from PIL import Image, ImageDraw, ImageFont
import random


class GenerateCode:
    def getcode(self):
        return chr(random.randint(65, 90))

    def backgroundcolor(self):
        return (random.randint(0, 165),
                random.randint(0, 165),
                random.randint(0, 165))

    def foregroundcolor(self):
        return (random.randint(125, 255),
                random.randint(125, 255),
                random.randint(125, 255))

    def genValidateCode(self):
        w, h = 240, 60
        panel = Image.new(size=(w, h), mode="RGB", color=(255, 255, 255))
        draw = ImageDraw.Draw(panel)
        font = ImageFont.truetype(r"C:\Windows\Fonts\ALGER.TTF", size=30)
        for y in range(h):
            for x in range(w):
                draw.point((x, y), fill=self.backgroundcolor())
        for i in range(4):
            draw.text((60*i+20, 15), text=self.getcode(), fill=self.foregroundcolor(), font=font)
        panel.show()


if __name__ == "__main__":
    generate = GenerateCode()
    generate.genValidateCode()