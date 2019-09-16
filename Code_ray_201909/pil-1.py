# 图片处理：
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

img = Image.open("dog.jpg")
print(img.format)  # 输出图片基本信息
print(img.mode)
print(img.size)
img_resize = img.resize((200, 200))  # 调整尺寸
img_resize.save("dogresize.jpg")
img_rotate = img.rotate(90)  # 旋转
img_rotate.save("dogrotate.jpg")
om = img.convert('L')  # 灰度处理
om.save('doggray.jpg')
om = img.filter(ImageFilter.CONTOUR)  # 图片的轮廓
om.save('dogcontour.jpg')
om = ImageEnhance.Contrast(img).enhance(20)  # 对比度为初始的10倍
om.save('dogencontrast.jpg')
# 更改图片格式：
from PIL import Image
import os

filelist = ["dog.jpg",
            "dogcontour.jpg",
            "dogencontrast.jpg",
            "doggray.jpg",
            "dogresize.jpg",
            "dogrotate.jpg",
            ]
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)