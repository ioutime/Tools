# **Script_Annotation**<br>

**功能:自动生成文件顶部注释**<br>
     eg:<br>'''<br>
        @FILE    :   main.py<br>
        @DSEC    :   自动生成文件顶部注释<br>
        @AUTHOR  :   ioutime<br>
        @DATE    :   2021/01/04  12:21:51<br>
        @VERSION :   1.0<br>
        '''<br>


**用法：** <br>
    1、可以将main.py和picture.py放在同一个目录下,运行main.py<br>
    2、直接运行打包结果里的exe程序<br>
<br>
***
## 解决pyinstaller打包图片

这个功能其实没什么太大用,就是写着玩,写这个工具时解决了pyinstaller打包图片的问题。<br>
问题描述：如何将图片也一起打包到exe文件中<br>

解决思路：将图片转成py文件,将其看成一个包导入<br>
    1、将图片转成py文件,eg：picture.py,就是图片用base64<br>
    2、在要打包的main.py文件中代码加入 **from xxx import img**<br>
    3、将picture.py 和main.py文件放在同一个目录下,执行：pyinstaller -f -w main.py
