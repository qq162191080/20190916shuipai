from tkinter import *

root = Tk()

# 获取屏幕分辨率
# print(root.winfo_screenwidth())

# print(root.winfo_screenheight())

#全屏
#root.attributes("-fullscreen", True)

closeApp=Canvas(root, width=10, height=10)
closeApp.create_oval(3, 3,10,10, fill="red",width=0)

closeApp.pack(anchor=NE)

def appClose(event):
    root.quit()
    
closeApp.bind("<ButtonRelease-1>",appClose)


photo = PhotoImage(file="001.png")

photo.zoom(2,3)


label_1=Label(root,text="Hello FishC!",height=200,image=photo)


label_1.pack()

mainloop()
