from io import BytesIO
import base64
from PIL import Image

img_name = input('Nome do Arquivo:')
img_format = input('Formato de Saída do Arquivo:')


with open(img_name, 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    # print(len(base64_bytes))

    im = Image.open(BytesIO(base64.b64decode(base64_bytes)))

    # print(f'Tipo: {type(im)} e {type(base64_bytes)}')
    match img_format:
        case 'png':
            im.save(f'{img_name}-convert.png', 'PNG')
        case 'jpg':
            rgb_im = im.convert('RGB')
            rgb_im.save(f'{img_name}-convert.jpg')
        case _:
            rgb_im = im.convert('RGB')
            rgb_im.save(f'{img_name}-convert.jpg')