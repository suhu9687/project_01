
# -*- coding: utf-8 -*-

"""

1、安装库 pip install pymupdf

2、直接运行

"""
import sys
import fitz
import pandas as pd
import glob as gb
from pathlib import Path
import os,shutil
from PIL import Image
import cv2
import re
import matplotlib.pyplot as plt

pdf_dir = []

def get_file():
    docunames = os.listdir()
    for docuname in docunames:
        if os.path.splitext(docuname)[1] == '.pdf':  # 目录下包含.pdf的文件
            pdf_dir.append(docuname)



def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        pdf_s = str(pdf)
        pdf_name = os.path.splitext(pdf)[0]
        pdf_name_1 = ''.join(filter(lambda c: ord(c) < 256, pdf_name))
        os.mkdir(pdf_name_1)  # 创建文件夹
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 1.0
            zoom_y = 1.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pg = str(pg + 1).zfill(2)
            pg_1 = str(pdf_name + pg)
            pm.writePNG('%s.png' % pg_1)
            png_name = str(('%s.png' % pg_1))
            print(na)
            #shutil.move(png_name, pdf_exe)  # 移动文件


if __name__ == '__main__':
    get_file()
    conver_img()