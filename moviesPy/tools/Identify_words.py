#coding:utf8
from PIL import Image
import pytesseract

'''
python 图像识别
PIL：（Python Imaging Library）是Python平台上的图像处理标准库，功能非常强大。
pytesseract：图像识别库。
python 3.x首先安装
pip install pytesseract
pip install pillow
然后安装tesseract-ocr引擎
IOS 直接 brew install tesseract；
windows安装包 https://digi.bib.uni-mannheim.de/tesseract/ 下载后就是一个exe安装包，直接右击安装即可
编辑 系统变量里面 path，添加下面的安装路径 C:\Program Files\Tesseract-OCR
通过tesseract -v看一下是否安装成成功
安装tesseract-ocr语言包
我们去GitHub下载我们需要的语言包，这里我只下载了chi_tra.traineddata和chi_sim.traineddata
github：tesseract-ocr/tessdata
然后放到/usr/local/Cellar/tesseract/3.05.01/share/tessdata路径下面
可以通过tesseract --list-langs查看本地语言包
运行python文件就可以看到效果了(只能识别一下简单的图片，识别度不是很高~)
'''

# img = Image.open("../img/pic.png")
img = Image.open("../img/code01.jpg") 
# img = Image.open("../img/code02.jpg")
# img = Image.open("../img/code03.png")
# img = Image.open("../img/carNum.jpg")
# img = Image.open("../img/code.png")

code = pytesseract.image_to_string(img,lang="chi_sim+eng")
print(code)