from PIL import Image, ImageDraw, ImageFont
from random import randint, random
import textwrap


class MemeEngine():

    def __init__(self, out_img_folder: str):
        self.out_img_folder = out_img_folder

    def make_meme(self, img_path, text, author, width=500):
        """Create a Meme With a quote

        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = self.read(img_path)
        print(f"img.size IZ {img.size}")

        if(width <= 500):
            img = self.resize_img(img, width)

        if text is not None:
            self.draw(img, text, author)

        tmp = f'./tmp/{randint(0, 100000000)}.png'

        img.save(self.out_img_folder + f"/{randint(0, 100000000)}.jpg")
        return self.out_img_folder + "/{randint(0, 100000000)}.jpg"

    def read(selfself, img_path):
        return Image.open(img_path)

    def resize_img(self, img, width):
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        return img.resize((width, height), Image.NEAREST)

    def draw(self, img, text, author):
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                  size=20)
        h, w = img.size
        four_fifths = w * .8
        one_fifth = w * .20
        rand_x = randint(1, four_fifths)
        if((len(text) * 6) > one_fifth):
            wrap_amount = one_fifth / 6
            text = textwrap.fill(text=text, width=wrap_amount)
            draw.text((rand_x + 10, rand_x + 80), author, font=font, fill='black')
        else:
            draw.text((rand_x + 10, rand_x + 40), author, font=font, fill='black')
        draw.text((rand_x, rand_x + 20), text, font=font, fill='yellow')
