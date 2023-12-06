from io import BytesIO
import base64
from PIL import Image
import os

def get_elements():
    lista = os.listdir()
    removerLista = ['venv','.py','.txt']
    for index,item in enumerate(lista):
        # print(f'Item {item} - Index:{index}')
        if item[0]== '.':
            lista.pop(index)

    for i in removerLista:
        for index,item in enumerate(lista):
            if i in item:
                lista.pop(index)


    return lista

foundElements = get_elements()

[print(f'{index+1} - {item}\n') for index, item in enumerate(foundElements)]

list_formats = ['png','jpg']

img_index = input('Insira o número do Arquivo:')

try:
    imagem = foundElements[int(img_index)-1]
except:
    print(f'Imagem não encontrada')
    exit()

img_format = input(f'Formato de Saída do Arquivo - {list_formats}:')

if img_format not in list_formats:
    print(f'Formato de extensão não aceito')
    exit()

with open(imagem, 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    # print(len(base64_bytes))

    im = Image.open(BytesIO(base64.b64decode(base64_bytes)))

    # print(f'Tipo: {type(im)} e {type(base64_bytes)}')
    match img_format:
        case 'png':
            im.save(f'{foundElements[int(img_index)-1]}-convert.png', 'PNG')
        case 'jpg':
            rgb_im = im.convert('RGB')
            rgb_im.save(f'{foundElements[int(img_index)-1]}-convert.jpg')
        case _:
            rgb_im = im.convert('RGB')
            rgb_im.save(f'{foundElements[int(img_index)-1]}-convert.jpg')
