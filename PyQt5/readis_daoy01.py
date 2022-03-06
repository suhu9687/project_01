from redis import *
if __name__=="__main__":
    try:
        #创建Redis对象，与redis服务器建⽴连接
        sr=Redis(host="localhost",
        port=6379,
        db=0)
        #添加键name，值为itheima
        result=sr.set('name','itheima')
        #输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)