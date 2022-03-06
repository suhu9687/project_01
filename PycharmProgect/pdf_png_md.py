# -*- coding: utf-8 -*-

"""

1、安装库 pip install pymupdf

2、直接运行

"""
import sys
import re
import fitz
import pandas as pd
import os
import glob as gb
from pathlib import Path
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
        pdf_s = str(pdf)
        pdf_name = os.path.splitext(pdf)[0]
        file_exe = ('%s/imang' % pdf_name)
        os.mkdir(pdf_name) # 创建文件夹
        os.mkdir(file_exe)
        #shutil.move(pdf_s, file_exe)  # 移动文件
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 1.0
            zoom_y = 1.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pg = str(pg + 1).zfill(2)
            pm.writePNG('%s.png' % pg)

            '''下面的为写mdr的内容'''
            sys.path.append('E:\\Anaconda\\libs')
            # 存放原始图片地址

            data_base_dir = file_exe

            file_list = []  # 建立列表，用于保存图片信息

            # 读取图片文件，并将图片地址、图片名和标签写到txt文件中

            write_file_name = ('%s/dir.md' % file_exe)

            write_file = open(write_file_name, "w")  # 以只写方式打开write_file_name文件

            for file in os.listdir(data_base_dir):  # file为current_dir当前目录下图片名

                if file.endswith(".png"):  # 如果file以jpg结尾

                    write_name = file  # 图片路径 + 图片名 + 标签

                    file_list.append(write_name)  # 将write_name添加到file_list列表最后

                    sorted(file_list)  # 将列表中所有元素随机排列

                number_of_lines = len(file_list)  # 列表中元素个数

            # 将图片信息写入txt文件中，逐行写入

            for current_line in range(number_of_lines):
                current_line_str = str(file_list[current_line])

                pig_init = str('![](imang/%s)' % current_line_str)

                write_file.write(pig_init + '\n')

            write_file.close()  # 关闭文件

            p = os.listdir()  # 初始化构造Path对象
            FileList = list(gb.glob("*.png"))  # 得到该目录下的所有的png文件
            print(FileList)
            # print (type(FileList))
            for filename in FileList:  # 遍历所有的png文件名
                filename_txt = str(filename)
                print(filename)
                shutil.move(filename_txt, file_exe)  # 移动文件

        write_file_name = str('SUMMARY.md')
        write_file = open(write_file_name, "a")
        pdf_name_md = str('(%s/dir.md)' % pdf_name)
        pig_init = str('* [%s]' % pdf_name)
        write_file.write(pig_init + pdf_name_md + '\n')

    write_file.close()  # 关闭文件

def move_md():
    for pdf in pdf_dir:
        pdf_name = os.path.splitext(pdf)[0]
        file_exe = ('%s/imang' % pdf_name)
        path_d = str("C:/Users/Think/Desktop/PycharmProgect/%s" % file_exe)
        path_s = str("C:/Users/Think/Desktop/PycharmProgect/%s" % pdf_name)
        filelist = os.listdir(path_d)
        for file in filelist:
            if os.path.splitext(file)[1] == ".md":
                md_md = str(file)
                src = os.path.join(path_d, md_md)
                shutil.move(src, path_s)  # 移动文件


if __name__ == '__main__':
    get_file()
    conver_img()
    move_md()

