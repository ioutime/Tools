import os
import time
import base64
import tkinter as tk
from picture import img#自己的包
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox


#新建文章
def newpage():
    pagetitle  = function0.get()
    os.system('hexo new '+pagetitle +'&& ping -n 5 www.baidu.com')

# 渲染
def generate():
    os.system('hexo g'+'&& ping -n 10 www.baidu.com')
#推送
def push():
    os.system('hexo d'+'&& ping -n 10 www.baidu.com')


root = tk.Tk()
root.title('Blog’s Tool')
root.geometry('+1000+350')
root.geometry('260x160')
root.resizable(width=False, height=False)
# ico图片
try:
    iou = open("iou.ico","wb+")
    iou.write(base64.b64decode(img))
    iou.close()
    root.iconbitmap("iou.ico")
    os.remove("iou.ico")
except:
    pass
logo = Label(root,text='Hexo',font=('华文隶书',20))
logo.place(x=100,y=10)

act = Label(root,text='名字',font=('华文行楷',17))
act.place(x=25,y=50)
function0 = StringVar()
entry = Entry(root,width='13',font=('黑体',18),textvariable=function0)  # 设置"文本变量"为var
entry.place(x=85,y=50)

s = Button(root,text='新建',font=('华文行楷',15),bd=1,command = newpage)
s.place(x=40,y=90)

w = Button(root,text='渲染',font=('华文行楷',15),bd=1,command = generate)
w.place(x=100,y=90)

q = Button(root,text='推送',font=('华文行楷',15),bd=1,command = push)
q.place(x=160,y=90)



root.mainloop()
