import os
import shutil
from PIL import Image
import cv2
import re
import glob as gb
import matplotlib.pyplot as plt
import fitz

def getFileList(dir, Filelist, ext=None):#获取文件下面的所有指定文件
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

def Picture_conversion(imglist): # 图片转换(png转jpg)
    for imgpath in imglist:
        imgname_path, old_png = os.path.split(imgpath)  # 获取的是图片路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        new_name = ('%s.jpg' % imgname)
        new_jpg = os.path.join(imgname_path, new_name)
        print(old_png)
        im = Image.open(imgpath)
        rgb_im = im.convert('RGB')
        rgb_im.save(new_jpg)
        os.remove(imgpath)  # 删除老png文件
    imglist.clear()



def rename_file(dic_list):
    for jpg_path in jpg_list:
        list_mulu = []
        imgname_path, img_tup = os.path.split(jpg_path)  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(jpg_path))[0]  # 获取的为文件名不包含后缀
        # 只保留中文、大小写字母和阿拉伯数字,获取来用于创建目录
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_eng = ''.join(filter(lambda c: ord(c) < 256, imgname))  # 无中文字
        imgname_new = (re.sub(reg, '', imgname_eng))#获取来用做创建目录
        img_tup_cc = re.sub(reg, '', imgname) # 获取来用做字典键
        img_tup_kk = os.path.join(imgname_path, img_tup_cc)
        file_newname = '%s.jpg' % img_tup_cc
        file_new = '%s.jpg' % img_tup_kk
        try:
            os.rename(jpg_path, file_new)  # 创建文件夹
        except OSError:#
            pass


        #print(file_new)
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '一', '二', '三', '四', '五']
        list_cut = str(img_tup_kk[-1])
        if list_cut in num_list:
            keys = list(dic.keys())
            img_tup_kk = img_tup_kk[:-1]
            if img_tup_kk not in keys:
                dic.update({img_tup_kk: [file_newname]})
            if img_tup_kk in keys:
                (dic.get(img_tup_kk)).append(file_newname)

        else:
            dic.update({img_tup_kk: [file_newname]})
    imglist.clear()
    getFileList(org_img_folder, jpg_list, 'jpg')




def makepath_move_pg():
    for kk, vv in dic.items():
        kk_mm = kk.split('\\')
        kk_mulu = kk_mm[-1]
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        kk_p = ''.join(filter(lambda c: ord(c) < 256, kk_mulu))  # 无中文字
        kk_p = re.sub(reg, '', kk_p)
        kk_3 = os.path.split(kk)[0]
        new_path = os.path.join(kk_3, kk_p)
        # print(new_path)
        # print(vv)
        try:
            os.mkdir(new_path)  # 创建文件夹
        except OSError:
            pass

        for vv_jpg in vv:
            old_path = os.path.join(kk_3, vv_jpg)
            try:
                shutil.move(old_path, new_path)
            except OSError:
                pass

def he_chen_jpg(jpg_list):

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
        if len(Gpg_pic) >= 2:
            image_merge(Gpg_pic)

def Modify_file_name(imglist): # 修改文件名
    for imgpath in imglist:
        imgname_path = os.path.split(imgpath)[0]  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        # 只保留中文、大小写字母和阿拉伯数字
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', imgname))
        # imgname_nwe = ''.join(filter(lambda c: ord(c) < 256, imgname))
        imgname_newstr = str('%s.jpg' % imgname_new)
        new_file = os.path.join(imgname_path, imgname_newstr)
        try:
            os.rename(imgpath, new_file)
        except OSError:
            pass

def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdf)
        pdf_path = os.path.split(pdf)[0]
        pdf_name = os.path.splitext(os.path.basename(pdf))[0]  # 获取的为文件名不包含后缀
        pdf_name_1 = ''.join(filter(lambda c: ord(c) < 256, pdf_name))
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', pdf_name_1))  # 获取来用做目录
        path_new = os.path.join(pdf_path, imgname_new)
        try:
            os.mkdir(path_new)  # 创建文件夹
        except OSError:
            pass
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
            pm.writePNG('%s.jpg' % pg_1)
            p = os.listdir()  # 初始化构造Path对象
            FileList = list(gb.glob("*.jpg"))  # 得到该目录下的所有的png文件
            # print (type(FileList))
            for filename in FileList:  # 遍历所有的png文件名
                filename_txt = str(filename)

                shutil.move(filename_txt, path_new)  # 移动文件


def Modify_file_name(imglist): # 修改文件名
    for imgpath in imglist:
        imgname_path = os.path.split(imgpath)[0]  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        # 只保留中文、大小写字母和阿拉伯数字
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', imgname))
        # imgname_nwe = ''.join(filter(lambda c: ord(c) < 256, imgname))
        imgname_newstr = str('%s.jpg' % imgname_new)
        new_file = os.path.join(imgname_path, imgname_newstr)
        try:
            os.rename(imgpath, new_file)
        except OSError:
            pass
    imglist.clear()
    getFileList(org_img_folder, jpg_list, 'jpg')

def he_chen_jpg(jpg_list):

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
        if len(Gpg_pic) >= 2:
            #resize_by_width(Gpg_pic, 1080, jpg_list) #停用后image_merge(Gpg_pic) 不停为jpg_list
            image_merge(Gpg_pic)
    imglist.clear()
    getFileList(org_img_folder, jpg_list, 'jpg')


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
        #imgname = ''.join(filter(lambda c: ord(c) < 256, imgname_zw)) # 剔除中文
        imgname_1 = ('%spg.jpg' % imgname)
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

    try:
        if not os.path.exists(imgname_path):
            os.makedirs(imgname_path)
        save_path = os.path.join(imgname_path, imgname_1)
        new_img.save(save_path)
    except OSError:
        pass

    for img_pg in Gpg_pic:
        if not img_pg[-8:] == 'Hcpg.jpg':
            os.remove(img_pg)
    return save_path

def image_resize(img, size=(1500, 1100)):
    """调整图片大小
    """
    try:
        if img.mode not in ('L', 'RGB'):
            img = img.convert('RGB')
        img = img.resize(size)
    except Exception:
        #print(imgname_1)
        pass
    return img

def wite_md_path():
    for imgpath in jpg_list:
        dic = {}
        list_mulu = []
        imgname_path, img_tup = os.path.split(imgpath)  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(imgpath))[0]  # 获取的为文件名不包含后缀
        # 只保留中文、大小写字母和阿拉伯数字
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        imgname_new = (re.sub(reg, '', imgname))#获取来用做目录
        imgname_eng = imgname_nwe = ''.join(filter(lambda c: ord(c) < 256, imgname_new))#无中文字
        imgname_str = str('%s.jpg' % imgname_eng)
        new_path = os.path.join(imgname_path, imgname_str)
        list_mulu = new_path.split('PycharmProgect\\')
        mulu_luj = list_mulu[-1]
        print(mulu_luj)
        try:
            os.rename(imgpath, new_path)
        except OSError:
            pass
        dic.update({imgname_new: imgname_eng})
        for kk, vv in dic.items():
            mu_lu = str('* [%s]' % kk)
            m_c = str('%s.md' % vv)
            pj_nr = str('![](%s)' % mulu_luj)
            m_c = str('%s.md' % vv)
            kuo_x = ('(%s)' % m_c)
            mu_lu_1 = str(mu_lu + kuo_x)


        with open(m_c, 'a+') as org_img_folder:
            org_img_folder.write(pj_nr + '\n')

        with open('SUMMARY.md', 'a+') as org_img_folder:
            org_img_folder.write(mu_lu_1 + '\n')


def resize_by_width(Gpg_pic, w_divide_h, jpg_list):
    """按照宽度进行所需比例缩放"""
    for path_jpg in Gpg_pic:
        print(path_jpg)
        imgname_path = os.path.split(path_jpg)[0]  # 获取的是图片的路径
        imgname = os.path.splitext(os.path.basename(path_jpg))[0]  # 获取的为文件名不包含后缀
        imgname_newstr = '%s.png' % imgname
        nwe_name = os.path.join(imgname_path, imgname_newstr)
        im = Image.open(path_jpg)
        (x, y) = im.size
        x_s = w_divide_h
        y_s = int(x / w_divide_h * y)
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(nwe_name)
        os.remove(path_jpg)

    imglist.clear()
    getFileList(org_img_folder, jpg_list, 'png')

    return Gpg_pic





if __name__ == '__main__':
    jpg_list = []
    dic = {}
    pdf_dir = []
    org_img_folder = r"C:\Users\Think\Desktop\PycharmProgect"
    getFileList(org_img_folder, pdf_dir, 'pdf')
    conver_img()
    imglist = getFileList(org_img_folder, jpg_list, 'png')
    Picture_conversion(imglist)
    #imglist = getFileList(org_img_folder, jpg_list, 'jpg')
    #rename_file(dic)
    #makepath_move_pg()
    #Modify_file_name(imglist)
    #he_chen_jpg(jpg_list)
    #wite_md_path()
