博客提交工具
---

介绍：
---

这个工具，是在你使用hexo搭建博客完成后，可以帮助你完成

- 创建新文章
- 渲染
- 推送

使用方法
---

将[blog.exe](https://github.com/ioutime/Tools/blob/master/blog-hexo/打包结果/blog.exe)复制到你博客创建的文件夹下，为其创建快捷键，将快捷键放在好打开的位置上。


![](/img/blog.png)

双击打开刚刚创建的快捷键就可以使用了。

```shell
#打包命令
Pyinstaller -F -w -i .\favicon.ico .\blog.py