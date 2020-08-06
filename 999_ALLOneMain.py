from requests import post
import base64
import json

from PIL import Image

# Шаг 1
def POSTpngSave(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0', 
    'Accept': '*/*', 
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
    'authToken': '0173b849-3cf7-1cac-852', # Заменить на акктуальный
    'deviceId': 'test-PC', 
    'deviceType': 'DESKTOP', 
    'UI-Version': '1.1', 
    'Content-Type': 'application/json', 
    'Content-Length': '76', 
    'Origin': 'https://url.ru', 
    'Connection': 'keep-alive',
    'Referer': 'https://url.ru/', 
    'Host': 'url.ru'
    }
    proxies={'https': 'https://127.0.0.1:8080'}
    payload={'placement':'PASSWORD_RECOVERY'}
#    post2 = post('https://url.ru/captcha', headers=headers, json = payload, proxies=proxies, verify=False) # С прокси
    post2 = post('https://url.ru/captcha', headers=headers, json = payload, verify=False) #Без прокси
    b=[]
    d=str(post2.json())
    b=d.split(',')
#    print(b)
    p=b[3]
    img=p[0:-1]
    imgB=img.encode('utf-8')
    with open('img/'+str(i)+'.png', 'wb') as file_to_save:
        imgD=base64.decodebytes(imgB)
        file_to_save.write(imgD)
    #print(b)
    file_to_save.close()

#Шаг 2

def CleanCapt(i):
    image = Image.open('img/'+str(i)+'.png').convert("L")
    pixel_matrix = image.load()
    
    # Очистка по принцыпу если не черный (0) значит белый (255). Так убираем затемнения
    for column in range(0, image.height):
        for row in range(0, image.width):
            if pixel_matrix[row, column] != 0:
                pixel_matrix[row, column] = 255


    # stray line and pixel removal
    for column in range(1, image.height - 1):
        for row in range(1, image.width - 1):
            if pixel_matrix[row, column] == 0 \
                and pixel_matrix[row, column - 1] == 255 and pixel_matrix[row, column + 1] == 255:
                pixel_matrix[row, column] = 255
            if pixel_matrix[row, column] == 0 \
                and pixel_matrix[row - 1, column] == 255 and pixel_matrix[row + 1, column] == 255:
                pixel_matrix[row, column] = 255

    image.save('imgClean/'+str(i)+'.png')
    
#Шаг 5

def main(img):
    """main"""

    # Opening the Image, convertring to grayscale
    image = Image.open("imgClean/"+str(img)+".png").convert("L")
    with open("AlphMapJSON\AlphabetMap.json", "r") as fin:
        bitmap = json.load(fin)

    # Какие символы в капче
    characters = "0123456789"
    captcha = ""

    i=18  #Начало алфовита в пикселях
    j=40  #Конец первого символа в пикселях
    height=12 # Верхная граница символа
    low=45 # Нижная граница символов
    
    # parses every character, 6 is number of characters
    kol=1
    while kol<7:
        char_img = image.crop((i, height, j, low))
        char_matrix = char_img.load()
        matches = {}
        for char in characters:
            match = 0
            black = 0
            bitmap_matrix = bitmap[char]
            for col in range(0, 32):    #Размеры матрицы алфовита
                for row in range(0, 22):
                    if char_matrix[row, col] == bitmap_matrix[col][row] \
                        and bitmap_matrix[col][row] == 0:
                        match += 1
                    if bitmap_matrix[col][row] == 0:
                        black += 1
            perc = float(match) / float(black)
            matches.update({perc: char[0].upper()})
        try:
            captcha += matches[max(matches.keys())]
        except ValueError:
            print("failed captcha")
            captcha += "0"
        
        i=i+22  #22 в данном случае это стандартная ширина символа в алфовите
        if captcha=="1":
            i=i-5
        elif captcha=="7":
            i=i-2
        elif captcha=="6":
            i=i-1    
        j=i+22
        
        kol=kol+1
 
    return captcha


if __name__ == '__main__':
    i=0
    while i<100:
        POSTpngSave(i) # Шаг 1
        CleanCapt(i)   # Шаг 2
        print(main(i)) # Шаг 5
        i=i+1
