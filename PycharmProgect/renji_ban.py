import os,re




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

if __name__ == '__main__':
    org_img_folder = r"C:\Users\Think\Desktop\PycharmProgect"
    jpg_list = []
    imglist = getFileList(org_img_folder, jpg_list, 'jpg')


    for imgpath in imglist:
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


