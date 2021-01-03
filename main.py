import time
import os
import sys
import base64
import tkinter as tk
from logo import img#自己的包
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


def end():
    sys.exit()

def judge(): 
    file_path = askopenfilename()
    try:
        with open(file_path,'r+',encoding='UTF-8') as g:
            num = 0
            num2 = 0

            for line in g.readlines()[0:7]:
                line = line.strip() #去掉每行头尾空白
                if line.startswith('#') or line.startswith('//'):
                    num+=1       #有几行注释
                if line.startswith("'''") or line.startswith('/*'):
                    num2 = 2     
            g.close()
            if num >=4:
                a = messagebox.askyesno('提示', '可能已经有文件头注释，是否继续')#是/否，返回值true/false
                if a==True:
                    write_annotation(file_path)
            elif num2 ==2:
                b = messagebox.askyesno('提示', '可能已经有文件头注释，是否继续')#是/否，返回值true/false
                if b==True:
                    write_annotation(file_path)
            else:
                write_annotation(file_path)
    except:
        messagebox.showwarning('提示','judge函数出错了')



def write_annotation(file_path): 
    try :
        with open(file_path,'r+',encoding='UTF-8') as f:
            filename = f.name
            filename = filename.split('/')[-1]
            function = function0.get()
            author = author0.get()
            version = version0.get()
            if function == '':
                function = '...'
            if author == '':
                author = '...'
            if version == '':
                version = '1.0'   
            date = time.strftime("%Y/%m/%d  %H:%M:%S",time.localtime())     
            content = f.read()
            f.seek(0, 0)
            signature = "'''\n\
@FILE    :   {0}\n\
@DSEC    :   {1}\n\
@AUTHOR  :   {2}\n\
@DATE    :   {3}\n\
@VERSION :   {4}\n\
'''\n".format (filename,function,author,date,version)
            f.write(signature+content)
            messagebox.showinfo('提示','成功')
            f.close()
    except FileNotFoundError:
        messagebox.showwarning('提示','路径未选择')
    except:
        messagebox.showwarning('提示','write_annotation函数出错了')


        

root = tk.Tk()
root.title('精灵球')
root.geometry('+300+150')
root.geometry('350x250')
root.resizable(width=False, height=False)
try:
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root.iconbitmap("tmp.ico")
    os.remove("tmp.ico")
    # root.iconbitmap(default = r'精灵球.ico')
except:
    pass
logo = Label(root,text='Welcome To Use',font=('华文行楷',20))
logo.place(x=100,y=10)

act = Label(root,text='功能',font=('华文行楷',17))
act.place(x=65,y=50)
function0 = StringVar()
entry = Entry(root,width='13',font=('黑体',18),textvariable=function0)  # 设置"文本变量"为var
entry.place(x=135,y=50)



act2 = Label(root,text='作者',font=('华文行楷',17))
act2.place(x=65,y=90)
author0 = StringVar()
entry2 = Entry(root,width='13',font=('黑体',18),textvariable=author0)  # 设置"文本变量"为var
entry2.place(x=135,y=90)



act3 = Label(root,text='版本',font=('华文行楷',17))
act3.place(x=65,y=130)
version0 = StringVar()
entry3 = Entry(root,width='13',font=('黑体',18),textvariable=version0)  # 设置"文本变量"为var
entry3.place(x=135,y=130)


s = Button(root,text='选择文件',font=('华文行楷',15),bd=1,command=judge)
s.place(x=90,y=180)
q = Button(root,text='退出',font=('华文行楷',15),bd=1,command=end)
q.place(x=220,y=180)
root.mainloop()



