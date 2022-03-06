import win32com
import win32com.client
import sys
import os
import re
from PIL import Image

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
            if ext in dir[-4:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


def getFileList_1(dir, Filelist, ext=None):#获取文件下面的所有指定文件
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



def ppt2png(ppt_list):
    path = sys.path[0]
    JPG_list = []
    for ppt_name in ppt_list:
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]" # 只保留数字和中文用于.md目录
        ppt_root = jpg_root = os.path.split(ppt_name)[0] +'/'
        pptFileName = os.path.splitext(os.path.basename(ppt_name))[0]  # 获取的为文件名不包含后缀
        powerpoint = win32com.client.Dispatch('PowerPoint.Application')
        powerpoint.Visible = True
        file_name = ''.join(filter(lambda c: ord(c) < 256, pptFileName.rsplit('.')[0]))#无中文字
        md_name = re.sub(reg, '', pptFileName.rsplit('.')[0])
        ppt_path = os.path.join(ppt_root, file_name)
        #outputFileName = pptFileName[0:-4] + ".pdf"
        ppt = powerpoint.Presentations.Open(ppt_name)
        #保存为图片
        ppt.SaveAs(jpg_root + file_name + '.jpg', 17)
        #保存为pdf
        #ppt.SaveAs(jpg_root + outputFileName, 32) # formatType = 32 for ppt to pdf
        # 关闭打开的ppt文件
        ppt.Close()
        # 关闭powerpoint软件

        getFileList_1(path, JPG_list, 'JPG')

        for jpg_J in JPG_list:
            num = str(JPG_list.index(jpg_J) + 1).zfill(2)
            jpg_path = os.path.split(jpg_J)[0]
            jpg_name = os.path.splitext(os.path.basename(jpg_J))[0]
            jpg_name_s = md_name + ('%s.png' % num)
            new_name = os.path.join(jpg_path, jpg_name_s)
            try:
                os.rename(jpg_J, new_name)
            except OSError:
                pass


        JPG_list.clear()

    powerpoint.Quit()

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
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '二', '三', '四', '五']
        list_cut = str(img_tup_kk[-1])
        if list_cut in num_list:
            keys = list(dic.keys())
            img_tup_kk = img_tup_kk[:-2]
            if img_tup_kk not in keys:
                dic.update({img_tup_kk: [file_newname]})
            if img_tup_kk in keys:
                (dic.get(img_tup_kk)).append(file_newname)

        else:
            dic.update({img_tup_kk: [file_newname]})
    imglist.clear()
    getFileList(org_img_folder, jpg_list, 'jpg')

def make_md():
    for kk, vv in dic.items():
        kk, kk_1 = os.path.split(kk)
        print(kk)
        mu_lu = str('* [%s]' % kk_1)
        for file_name in vv:
            imgpath = os.path.join(kk, file_name)
            new_nam = ''.join(filter(lambda c: ord(c) < 256, file_name.split('.')[0]))
            new_name = os.path.join(kk, new_nam)
            new_name_1 = str('%s.jpg' % new_name)
            list_mulu = kk.split('PycharmProgect\\')
            new_name_2 = new_name_1.split('PycharmProgect\\')[-1]
            mulu_luj = list_mulu[-1]
            os.rename(imgpath, new_name_1)
            m_c = str('%s.md' % mulu_luj)
            pj_nr = str('![](%s)' % new_name_2)
            kuo_x = ('(%s)' % m_c)
            mu_lu_1 = str(mu_lu + kuo_x)

            with open(m_c, 'a+') as org_img_folder:
                org_img_folder.write(pj_nr + '\n')

        with open('SUMMARY.md', 'a+') as org_img_folder:
            org_img_folder.write(mu_lu_1 + '\n')



if __name__ == '__main__':
    jpg_list = []
    dic = {}
    ppt_dir = []
    org_img_folder = r"C:\Users\Think\Desktop\PycharmProgect"
    #ppt_list = getFileList(org_img_folder, ppt_dir, 'pptx')
    #ppt2png(ppt_list)
    imglist = getFileList_1(org_img_folder, jpg_list, 'png')
    Picture_conversion(imglist)
    imglist.clear()
    getFileList_1(org_img_folder, jpg_list, 'jpg')
    rename_file(dic)
    make_md()
    imglist.clear()

