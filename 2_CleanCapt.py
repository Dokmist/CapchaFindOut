from PIL import Image


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



if __name__ == '__main__':
    i=0
    while i<10:
        CleanCapt(i)
        i=i+1