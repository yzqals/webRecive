import web

urls = (
    '/(.*)', 'hello'#域名与类的映射
)

app = web.application(urls, globals())


class hello:
    def POST(self,s):
        # 允许跨域访问
        web.header("Access-Control-Allow-Origin", "*")
        #获取FormData数据
        i = web.input()

        #将文件以原本的文件名保存
        data = i.get('file')#取出名为file的数据
        name = i.get('name')#取出名为name的数据，即文件名
        file = open(name, 'wb')#以二进制可写格式打开文件
        file.write(data)#数据写入文件
        file.close()#关闭文件

        #请随意写数据处理，
        #...
        #文件不用的话请自行写入删除代码

        return 'Hello,'#写返回值，返回值随意，可以把float转换为字符串后返回


if __name__ == "__main__":
    app.run()