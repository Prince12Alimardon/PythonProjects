# PythonProjects
This repository is my python projects

## 1. Generate Captcha in python
```shell
pip install captcha
# create python file and write this code
import string

from captcha.image import ImageCaptcha
from PIL import Image
import random


def generate_captcha_text(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length ))


def generate_captcha_image(captcha_text, image_width=300):
    image = ImageCaptcha(image_width)
    image_file = f"{captcha_text}.png"
    image.write(captcha_text, image_file)
    return image_file

captcha_text = generate_captcha_text()
image_file=generate_captcha_image(captcha_text)

print(f"GENERATED CAPTCHA")
Image.open(image_file).show()

```

## 2. Generate Barcode using python
```shell
# kerakli packagelar
pip install python-barcode
# python fayl yaratamiz va quyidagi kodni yozamiz
import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

barcode_format = barcode.get_barcode_class('ean13')
barcode_number = '12345678901202'
barcode_image = barcode_format(barcode_number, writer=ImageWriter())
barcode_filename = 'barcode_image'
barcode_image.save(barcode_filename)

display(Image(filename=f"{barcode_filename}.png"))

```
Nega aynan 'ean13'
```shell
'ean13' ni o'rniga quyidagilarni yozish mumkin.
* 'ean8': European Article Numbering (8 digits)
* 'ean13': European Article Numbering (13 digits)
* 'upc': Universal Product Code (12 digits)
* 'isbn10': International Standard Book Number (10 digits)
* 'isbn13': International Standard Book Number (13 digits)
* 'issn': International Standard Serial Number (8 digits)
* 'code39': Code 39
* 'code128': Code 128
* 'pzn': Pharmazentralnummer (Pharmacy Central Number)
```
