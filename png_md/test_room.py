import os
import re
import winerror
import cv2
from win32com.client.dynamic import Dispatch, ERRORS_BAD_CONTEXT


def corp_margin(jpg_list):
        "去除图像四周的留白"
        for JP in jpg_list:
            reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  # 只保留数字和中文用于字母
            JP_path, JP_name = os.path.split(JP)
            SAVE_Name = re.sub(reg, '', os.path.splitext(os.path.basename(JP))[0])  # 获取的为文件名不包含后缀
            save_name = '%s.jpg' % SAVE_Name
            save = os.path.join(JP_path, save_name)
            img = cv2.imread(JP)
            img2 = img.sum(axis=2)
            (row, col) = img2.shape
            row_top = 0
            row_down = 0
            col_top = 0
            col_down = 0
            for r in range(1, row, 10):
                if img2.sum(axis=1)[r] < 765 * col:
                    row_top = r - 18
                    break
            for r in range(row - 1, 0, -10):
                if img2.sum(axis=1)[r] < 765 * col:
                    row_down = r + 18
                    break
            for c in range(0, col, 10):
                if img2.sum(axis=0)[c] < 765 * row:
                    col_top = c - 18
                    break
            for c in range(col - 1, 0, -10):
                if img2.sum(axis=0)[c] < 765 * row:
                    col_down = c + 18
                    break
            new_img = img[row_top:row_down + 1, col_top:col_down + 1, 0:3]
            cv2.imwrite(JP, new_img)



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



def Adobe_jpg(pdf_list):
    ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)
    for pdf in pdf_list:
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  # 只保留数字和中文用于字母
        pdf_path, Pdf_name = os.path.split(pdf)
        pdf_Name = re.sub(reg, '', os.path.splitext(os.path.basename(pdf))[0])  # 获取的为文件名不包含后缀
        file_name = (''.join(filter(lambda c: ord(c) < 256, pdf_Name)))[:6]  # 无中文用于创建新文件
        try:
            os.mkdir(file_name)
        except Ellipsis:
            pass
        Jpg_name = '%s.jpg' % pdf_Name
        pdfsave_path = os.path.join(pdf_path, file_name)
        my_dir = pdf_path
        my_pdf = Pdf_name
        os.chdir(my_dir)
        src = os.path.abspath(my_pdf)
        try:
            AvDoc = Dispatch("AcroExch.AVDoc")

            if AvDoc.Open(src, ''):
                pdDoc = AvDoc.GetPDDoc()
                jsObject = pdDoc.GetJSObject()
                jsObject.SaveAs(os.path.join(pdfsave_path, Jpg_name), "com.adobe.acrobat.jpeg")

        except Exception as e:
            print(str(e))
        finally:
            AvDoc.Close(True)
            jsObject = None
            pdDoc = None
            AvDoc = None

if __name__ == '__main__':
    jpg_list = []
    dic = {}
    pdf_dir = []
    org_img_folder = r"C:\Users\Think\Desktop\png_md"
    #pdf_list = getFileList(org_img_folder, pdf_dir, 'pdf')
    #Adobe_jpg(pdf_list)
    jpg = getFileList(org_img_folder,jpg_list, 'jpg')
    corp_margin(jpg)
