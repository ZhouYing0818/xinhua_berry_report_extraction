#!/usr/bin/python
#coding:utf-8
#@ZHOU_YING
#2020-7-31
#PDF2image

from pdf2image import convert_from_path
import os
import sys
import PIL
import matplotlib.pyplot as plt
from PIL import ImageFont
from PIL import ImageDraw
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def merge_image(images,img_mun,height,width):
    to_image = PIL.Image.new('RGB', (2*width, (int(img_mun/2))*height), (255,255,255))
    n=0
    for i in range(int(img_mun/2)):
        for j in range(2):
            to_image.paste(images[n],(width*j,height*i))
            n+=1
            if n >=img_mun:
                break
    return to_image
    
def add_font(image,img_mun):
    font =ImageFont.truetype('/mnt/c/WINDOWS/Fonts/arial.ttf', 36)
    draw =ImageDraw.Draw(image)
    for t in range(int(img_mun/2+1)):
        for n in range(2):
            text='Chr '+str(t*2+n+1)
            position =(334*n,80*(t+1))
            draw.text(position, text, font=font, fill="#000000", spacing=0, align='left')
            if (t*2+n+1) >=img_mun:
                break
    return image
    
path="/mnt/d/pdf/"
print(path)
os.chdir(path)

dirslist=os.listdir()

for m in range(len(dirslist)):
    filename=dirslist[m]
    print(str(m)+'. '+filename+'  working...')
    if 'pdf' in filename:
        images=convert_from_path(filename,dpi=50)
        full_img=merge_image(images,24,87,334)
        wid = full_img.size[0]
        hei = full_img.size[1]
        full_img= full_img.resize((int(wid), int(hei)), PIL.Image.ANTIALIAS)
        #full_img=add_font(full_img,23)
        savepath=os.path.splitext(filename)[0]+'.jpg'
        full_img.save(savepath)