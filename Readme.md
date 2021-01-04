**Script_Annotation**
功能:自动生成文件顶部注释
     eg:'''
        @FILE    :   main.py
        @DSEC    :   自动生成文件顶部注释
        @AUTHOR  :   ioutime
        @DATE    :   2021/01/04  12:21:51
        @VERSION :   1.0
        '''
用法： 
    1、可以将main.py和logo.py放在同一个目录下,运行main.py
    2、直接运行打包结果里的exe程序

这个功能其实没什么太大用,就是写着玩,写这个工具时解决了pyinstaller打包图片的问题。
问题描述：如何将图片也一起打包到exe文件中
解决思路：将图片转成py文件,将其看成一个包导入
    1、将图片转成py文件,就是图片用base64
    2、
