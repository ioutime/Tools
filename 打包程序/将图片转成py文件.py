import base64
with open("精灵球.ico","rb") as f:
    strr = base64.b64encode(f.read())
    f.close()
    data = "img = %s" % strr
with open("picture.py","w+") as g:
    g.write(data)
    g.close()

