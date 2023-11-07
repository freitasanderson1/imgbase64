from io import BytesIO
import base64
from PIL import Image

img_name = input('Nome do Arquivo:')

with open(img_name, 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    print(base64_bytes)

    im = Image.open(BytesIO(base64.b64decode(base64_bytes)))
    im.save(f'{img_name}-convert.png', 'PNG')