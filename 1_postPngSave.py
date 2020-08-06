from requests import post
import base64
import json

from PIL import Image


def POSTpngSave(i):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0', 
    'Accept': '*/*', 
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
    'authToken': '0173b849-3cf7-1cac-852a', # Заменить на акктуальный
    'deviceId': 'test-PC', 
    'deviceType': 'DESKTOP', 
    'UI-Version': '1.1', 
    'Content-Type': 'application/json', 
    'Content-Length': '76', 
    'Origin': 'https://url', 
    'Connection': 'keep-alive',
    'Referer': 'https://url', 
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



if __name__ == '__main__':
    i=0
    while i<10:
        POSTpngSave(i)
#        print(main(i))
        i=i+1
