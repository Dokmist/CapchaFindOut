from requests import post
import json

from PIL import Image


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
    while i<10:
        print(main(i))
        i=i+1
