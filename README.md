# webRecive
利用web.py和js实现单独网页上的文件上传

# 使用方法
在服务器上安装web.py，在服务器上运行webTest.py，编写html和js使html里的元素id和js里对应

有人想要在一个从一个单独的未被布置在服务器上的html页面上上传图片到服务器

一开始的想法是通过websocket实现，但是python在收到的ArrayBuffer的解析上出现问题

最后是使用的web.py搭建简单的服务器，利用post请求实现文件的上传

# web.py的安装：http://webpy.org/install.zh-cn
