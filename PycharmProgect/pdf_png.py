# -*- coding: utf-8 -*-

"""

1、安装库 pip install pymupdf

2、直接运行

"""

import fitz

import glob as gb
from pathlib import Path
import os
from PIL import Image
import cv2
import re
import matplotlib.pyplot as plt
import shutil

pdf_dir = []

def get_file():
    docunames = os.listdir()
    for docuname in docunames:
        if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
            pdf_dir.append(docuname)



def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        pdf_name = os.path.splitext(pdf)[0]
        pdf_name_1 = ''.join(filter(lambda c: ord(c) < 256, pdf_name))
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', pdf_name_1))  # 获取来用做目录
        try:
            os.mkdir(imgname_new)  # 创建文件夹
        except OSError:
            pass

        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pg = str(pg + 1).zfill(2)
            pg_1 = str(pdf_name + pg)
            pm.writePNG('%s.jpg' % pg_1)
            p = os.listdir()  # 初始化构造Path对象
            FileList = list(gb.glob("*.jpg"))  # 得到该目录下的所有的png文件
            print(FileList)
            # print (type(FileList))
            for filename in FileList:  # 遍历所有的png文件名
                filename_txt = str(filename)
                print(filename)
                try:
                    shutil.move(filename_txt, imgname_new)  # 移动文件
                except OSError:
                    pass






if __name__ == '__main__':
    get_file()
    conver_img()