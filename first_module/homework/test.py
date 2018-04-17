#coding：utf-8
s = "路飞学城" # UTF-8类型，当在python2的windows 里面打印的时候，就会出现乱码。因为windows终端的格式是GBK
s2 = s.decode("utf-8")  #unicode 类型，utf-8 decode解码以后就变成了 unicode，就可以在windows终端打印
s3 = s2.encode("gbk") #gbk类型，unicode通过encode编码以后就变成了gbk类型，windows终端也是gbk类型，因此也可以打印
s4 = s2.encode("utf-8") #utf-8类型，unicode通过encode编码就变成了utf-8类型，在windows终端打印就乱码。
'''
在python2 里面打印出来的内容，不是unicode 就是 str类型。

python3 文件默认编码是  UTF-8
        字符串默认编码是 unicode
python2 文件默认编码是  ascii
        字符串默认编码是 ascii
        如果文件头声明了GBK，那字符串的编码是GBK
python2 里面unicode 是一个单独的类型
'''

