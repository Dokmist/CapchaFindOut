from PIL import Image



'''i=0
while i<5:
    cropped_image = image.crop((17+(i*23), 12, 39+(i*23), 47))
    cropped_image.save(str(i)+".png")
    i=i+1'''
def delicateRazbivka(i):
    image = Image.open('imgClean/'+str(i)+'.png').convert("L") # Grayscale conversion
    cropped_image = image.crop((15, 12, 39, 45)) # 1
    cropped_image.save("razbivkaCapt/1.png")

    cropped_image = image.crop((39, 13, 63, 45)) # 2
    cropped_image.save("razbivkaCapt/2.png")

    cropped_image = image.crop((60, 12, 84, 45)) # 3
    cropped_image.save("razbivkaCapt/3.png")

    cropped_image = image.crop((83, 12, 107, 45)) # 4
    cropped_image.save("razbivkaCapt/4.png")

    cropped_image = image.crop((107, 12, 131, 45)) # 5
    cropped_image.save("razbivkaCapt/5.png")

    cropped_image = image.crop((124, 12, 148, 45)) # 6
    cropped_image.save("razbivkaCapt/6.png")
    image.save('razbivkaCapt/0.png')
    
def delicateRazbivka2(i2):
    i=18
    j=i+22
    image = Image.open('imgClean/'+str(i2)+'.png').convert("L") # Grayscale conversion
    cropped_image = image.crop((i, 13, j, 45)) # 1
    cropped_image.save("razbivkaCapt/1.png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 2
    cropped_image.save("razbivkaCapt/2.png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 3
    cropped_image.save("razbivkaCapt/3.png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 4
    cropped_image.save("razbivkaCapt/4.png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 5
    cropped_image.save("razbivkaCapt/5.png")
    i=i+22-2
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 6
    cropped_image.save("razbivkaCapt/6.png")
    image.save('razbivkaCapt/0.png')


def loopRazbivka(i2):
    i=18
    j=i+22
    image = Image.open('imgClean/'+str(i2)+'.png').convert("L") # Grayscale conversion
    cropped_image = image.crop((i, 13, j, 45)) # 1
    cropped_image.save("razbivkaCapt/1/"+str(i2)+".png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 2
    cropped_image.save("razbivkaCapt/2/"+str(i2)+".png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 3
    cropped_image.save("razbivkaCapt/3/"+str(i2)+".png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 4
    cropped_image.save("razbivkaCapt/4/"+str(i2)+".png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 5
    cropped_image.save("razbivkaCapt/5/"+str(i2)+".png")
    i=i+22-2
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 6
    cropped_image.save("razbivkaCapt/6/"+str(i2)+".png")
    image.save('razbivkaCapt/'+str(i2)+'0.png')

def areOne(i2):
    i=18
    j=i+22
    image = Image.open('imgClean/'+str(i2)+'.png').convert("L") # Grayscale conversion
    cropped_image = image.crop((i, 13, j, 45)) # 1
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-1.png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 2
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-2.png")
    i=i+22
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 3
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-3.png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 4
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-4.png")
    i=i+22-1
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 5
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-5.png")
    i=i+22-2
    j=i+22
    cropped_image = image.crop((i, 13, j, 45)) # 6
    cropped_image.save("razbivkaCapt/areOne/"+str(i2)+"-6.png")
    image.save('razbivkaCapt/areOne/'+str(i2)+'_0.png')




if __name__ == '__main__':
    i=0
    while i<10:
        #delicateRazbivka(i) # Тонкая подгонка
        #delicateRazbivka2(i) №Тонкая подгонка в цикле
        #loopRazbivka(i)
        areOne(i)
        i=i+1