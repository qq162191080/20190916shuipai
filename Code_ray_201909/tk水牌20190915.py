from tkinter import *
# 图片缩放：
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

filename_A="001.png"
filename_B="001.png"
label_height=120
resize_xy=(90,120)


img = Image.open(filename_A)
print(img.format)  # 输出图片基本信息
print(img.mode)
print(img.size)

size_A=img.size
resize_xy=[int((label_height*size_A[0])/size_A[1]), label_height] #保持原比例
print(resize_xy)

img_resize = img.resize(resize_xy)  # 调整尺寸

print(img_resize)

img_resize.save(filename_A)

if img.format=="PNG":
    filename_B=filename_A
else:
    img_resize.save(filename_B)


root = Tk()

# 获取屏幕分辨率
# print(root.winfo_screenwidth())

# print(root.winfo_screenheight())

#全屏
root.attributes("-fullscreen", True)


closeApp=Canvas(root, width=10, height=10)
closeApp.create_oval(3, 3,10,10, fill="red",width=0)

closeApp.pack(anchor=NE)

def appClose(event):
    root.quit()
    
closeApp.bind("<ButtonRelease-1>",appClose)


photo = PhotoImage(file=filename_B)


label_1=Label(root,text="Hello FishC!",height=label_height,image=photo)


label_1.pack(anchor=W)

mainloop()
