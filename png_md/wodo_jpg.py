import os,shutil
from PIL import Image
import cv2
import re
import matplotlib.pyplot as plt

def getFileList_1(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
            print(Filelist)
                #getFileList(newDir, Filelist, ext)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)


def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist

def Modify_file_name(imglist): # 修改文件名
    for imgpath in imglist:
        imgname_path = os.path.split(imgpath)[0]  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        # 只保留中文、大小写字母和阿拉伯数字
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', imgname))
        imgname_newstr = str('%s.jpg' % imgname_new)
        new_file = os.path.join(imgname_path, imgname_newstr)
        try:
            os.rename(imgpath, new_file)
        except OSError:
            pass


        # 对每幅图像执行相关操作

def Picture_conversion(imglist): # 图片转换(png转jpg)
    for imgpath in imglist:
        imgname_path = os.path.split(imgpath)[0]  # 获取的是图片的名字
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        new_name = ('%s.jpg' % imgname)
        new_jpg = os.path.join(imgname_path, new_name)
        #print(new_jpg)
        im = Image.open(imgpath)
        rgb_im = im.convert('RGB')
        rgb_im.save(new_jpg)
        os.remove(imgpath)  # 删除老png文件

def image_merge(Gpg_pic, imgname_pat=None,imgname_1=None, restriction_max_width=None, restriction_max_height=None):
    """image_merge(images, output_dir='output', output_name='merge.jpg', \
    restriction_max_width=None, restriction_max_height=None):
    直合并多张图片
    images - 要合并的图片路径列表
    ouput_dir - 输出路径
    output_name - 输出文件名
    restriction_max_width - 限制合并后的图片最大宽度，如果超过将等比缩小
    restriction_max_height - 限制合并后的图片最大高度，如果超过将等比缩小"""
    for imgpath in Gpg_pic:
        imgname_path = os.path.split(imgpath)[0]  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        imgname_1 = ('%s合成图片.jpg' % imgname)
    print(imgname_path)

    img_list_1 = []
    max_width = 0
    total_height = 0
    # 计算合成后图片的宽度（以最宽的为准）和高度
    for img_path in Gpg_pic:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            width, height = img.size
            if width > max_width:
                max_width = width
            total_height += height

    # 产生一张空白图
    new_img = Image.new('RGB', (max_width, total_height), 255)

    # 合并
    x = y = 0
    for img_path in Gpg_pic:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            width, height = img.size
            new_img.paste(img, (x, y))
            y += height

    if not os.path.exists(imgname_path):
        os.makedirs(imgname_path)
    save_path = str('%s/%s' % (imgname_path, imgname_1))
    new_img.save(save_path)

    for img_pg in Gpg_pic:
        if not img_pg[-8:] == '合成图片.jpg':
            os.remove(img_pg)

if __name__ == '__main__':
    org_img_folder = r"C:\Users\Think\Desktop\PycharmProgect"

    # 检索文件
    jpg_list = []
    imglist = getFileList(org_img_folder, jpg_list, 'png')
    Picture_conversion(imglist)
    #print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
    imglist = getFileList(org_img_folder, jpg_list, 'jpg')
    Modify_file_name(imglist)
    newDir = []
    for jpg_pic in jpg_list:
        path_t, name_pg = os.path.split(jpg_pic)  # 获取的是图片的路径
        newDir.append(path_t)
        list_set = set([])  # 创建空集合
        for path_s in newDir:
            list_set.add(path_s)
            jpg_list_1 = list(list_set)
    for pig_jpg in jpg_list_1:
        p = os.listdir(pig_jpg)
        pig_jpg = str(pig_jpg)
        Gpg_pic = []
        for is_jpg in p:
            path_drss = os.path.join(pig_jpg, is_jpg)
            if path_drss[-4:] == '.jpg':
                Gpg_pic.append(path_drss)
        image_merge(Gpg_pic)




