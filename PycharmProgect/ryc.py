# client_id 为官网获取的AK， client_secret 为官网获取的SK
import requests
import base64
import re

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=8j8Fes4z7sIfB22aHQRRQZW7&client_secret=yqApFMrYrt9cWcEOZgNTRMZ6jxOQOY6C'
response = requests.get(host)
if response:
    print(response.json())
access_token = response.json()['access_token']
print(access_token)
'''
图像清晰度增强
'''
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
# 二进制方式打开图片文件
f = open(r'C:\Users\Think\Desktop\PycharmProgect\0914\09140\091404pg.jpg', 'rb')
img = base64.b64encode(f.read())


params = {"image": img}
#access_token = '24.403b919c26f73ca4f1bfdf7ace49927d.2592000.1648025240.282335-25640572'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json()['image'])

imgdata = base64.b64decode(response.json()['image'])
file = open(r'C:\Users\Think\Desktop\PycharmProgect\0914\09140\091404pggq.jpg', 'wb')
file.write(imgdata)
file.close()


