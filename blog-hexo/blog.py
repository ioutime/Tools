import os
import base64
import tkinter as tk
import webbrowser
from picture import img#自己的包
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox


#新建文章
def newpage():
    pagetitle  = function0.get()
    os.system('hexo new '+pagetitle +'&& ping -n 3 www.baidu.com')

# 渲染
def generate():
    os.system('hexo cl & hexo g'+'&& ping -n 10 www.baidu.com')
#推送
def push():
    os.system('hexo cl & hexo g & hexo d'+'&& ping -n 10 www.baidu.com')

#本地
def server():
    webbrowser.open("http://localhost:4000")
    os.system('hexo cl & hexo g & hexo s')

#备份
def backup():
    os.system('''git add . & git commit -m "update" & git push origin hexo'''+'&& ping -n 4 www.baidu.com')

#拉取 _post
def pull_post():
    os.system('''git pull origin hexo'''+'&& ping -n 4 www.baidu.com')

#推送 _post
def push_post():
    os.system('''git add .\source\_posts\* & git commit -m "update" & git push origin hexo'''+'&& ping -n 4 www.baidu.com')

root = tk.Tk()
root.title('Blog’s Tool')
root.geometry('+1000+350')
root.geometry('290x220')
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
logo.place(x=120,y=10)

act = Label(root,text='名字',font=('华文行楷',17))
act.place(x=25,y=50)
function0 = StringVar()
entry = Entry(root,width='13',font=('黑体',18),textvariable=function0)  # 设置"文本变量"为var
entry.place(x=85,y=50)

s = Button(root,text='新建',font=('华文行楷',15),bd=1,command = newpage)
s.place(x=30,y=90)

w = Button(root,text='渲染',font=('华文行楷',15),bd=1,command = generate)
w.place(x=110,y=90)

b = Button(root,text='本地',font=('华文行楷',15),bd=1,command = server)
b.place(x=190,y=90)

bk = Button(root,text='备份',font=('华文行楷',15),bd=1,command = backup)
bk.place(x=75,y=135)

q = Button(root,text='推送',font=('华文行楷',15),bd=1,command = push)
q.place(x=155,y=135)

bk = Button(root,text='pull_post',font=('Hermit',15),bd=1,command = pull_post)
bk.place(x=30,y=180)

q = Button(root,text='push_post',font=('Hermit',15),bd=1,command = push_post)
q.place(x=155,y=180)



root.mainloop()
