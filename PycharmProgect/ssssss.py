import cv2
import re

def corp_margin(img):
    "去除图像四周的留白"
    img2 = img.sum(axis=2)
    (row, col) = img2.shape
    row_top = 0
    row_down = 0
    col_top = 0
    col_down = 0
    for r in range(1, row, 10):
        if img2.sum(axis=1)[r] < 765 * col:
            row_top = r - 40
            break          
    for r in range(row-1, 0, -10):
        if img2.sum(axis=1)[r] < 765 * col:
            row_down = r - 40
            break    
    for c in range(0, col, 10):
        if img2.sum(axis=0)[c] < 765 * row:
            col_top = c - 40
            break    
    for c in range(col-1, 0, -10):
        if img2.sum(axis=0)[c] < 765 * row:
            col_down = c + 40
            break 
    new_img = img[row_top:row_down+1, col_top:col_down+1, 0:3]
    return new_img

im = cv2.imread(r'C:\Users\Think\Desktop\png_md\wlm20\wlm20.jpg')
img_re = corp_margin(im)
cv2.imwrite(r'C:\Users\Think\Desktop\png_md\wlm20\result.jpg', img_re)

