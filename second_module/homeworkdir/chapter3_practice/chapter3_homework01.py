'''
文件处理相关

1.编码问题

1.1 请说明python2 与python3中的默认编码是什么？
1.2 为什么会出现中文乱码？你能列举出现乱码的情况有哪几种？
1.3 如何进行编码转换？
1.4 #-*-coding:utf-8-*- 的作用是什么？
1.5 解释py2 bytes vs py3 bytes的区别

2.文件处理
2.1 r和rb的区别是什么？
2.2 解释一下以下三个参数的分别作用
 open(f_name,'r',encoding="utf-8")
'''


'''
#q1.1
python2 默认编码是 ASCII，python默认编码是 UTF-8

#q1.2
本人觉得之所以会有乱码，是因为人眼看到的乱码，在终端现实时才会被看见。那么会出现乱码的原因是什么呢？那就是字符的编码
格式和终端的编码格式不同导致。在python3中，会把文件编码自动转换成Unicode类型，因此，大多数乱码都出现在python2中
例如：文件编码ASCII编码格式，而终端是GBK，那么，就会出现乱码。文件编码是UTF-8 类型，终端是GBK也会出现乱码。

#q1.3
UTF-8 类型的字符编码转换(解码)成unicode ，则需要用到  decode('UTF-8')
a = "中文" （UTF-8类型） a2 = a.decode('utf-8'),那么a2就变成了 unicode类型。
a3 = a2.encode('GBK') 那么a3，就被编码成为了GBK类型。

#q1.4
#-*-coding:utf-8-*- 主要是声明文件编码是utf-8类型的。在python2 中，如果不加这个，默认是ASCII类型，
在python3中不加这个，也是默认是UTF-8类型。

#q1.5
http://m.blog.csdn.net/zengchen73/article/details/75302301
py2：
    str = bytes
    为什么有bytes？
        是因为要表示图片，视频等二进制格式的数据
        以UTF-8编码的字符串，在windows上不能显示
        如何在python2实现写一个软件，在全球各国电脑上，直接看？
        以unicode 编码写你的软件
        s = your_str.decode('utf-8')

        unicode类型

        文件头
        py2：以UTF-8 or GBK等的编码的代码，代码内容加载到内存，并不会被转成unicode，编码依然是 utf-8 or gbk等
        py3：以UTF-8 or GBK等的编码的代码，代码内容加载到内存，会被自动转成unicode
py3：str=unicode




'''



