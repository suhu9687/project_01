# 10. 实现代理池的API模块
- `目标`: 
    - 为爬虫提供高可用代理IP的服务接口

- `步骤`: 
   - 实现根据协议类型和域名, 提供随机的获取高可用代理IP的服务
   - 实现根据协议类型和域名, 提供获取多个高可用代理IP的服务
   - 实现给指定的IP上追加不可用域名的服务 

- `实现`:
   - 在proxy_api.py中, 创建`ProxyApi`类
   - 实现初始方法
     - 初始一个Flask的Web服务
     - 实现根据协议类型和域名, 提供随机的获取高可用代理IP的服务
        - 可用通过 `protocol` 和 `domain` 参数对IP进行过滤
        - `protocol`: 当前请求的协议类型
        - `domain`: 当前请求域名
     - 实现根据协议类型和域名, 提供获取多个高可用代理IP的服务
        - 可用通过`protocol` 和 `domain` 参数对IP进行过滤
     - 实现给指定的IP上追加不可用域名的服务 
       - 如果在获取IP的时候, 有指定域名参数, 将不在获取该IP, 从而进一步提高代理IP的可用性.
  - 实现run方法, 用于启动Flask的WEB服务
  - 实现start的类方法, 用于通过类名, 启动服务

- `完整代码`

```py
from flask import Flask
from flask import request
import json
from db.mongo_pool import MongoPool
import settings

class ProxyApi(object):
    def __init__(self):
        # 初始一个Flask的Web服务
        self.app = Flask(__name__)
        self.proxy_pool = MongoPool()

        @self.app.route('/random')
        def random():
            # 从传入参数中获取URL
            # 根据protocol参数获取协议
            protocol = request.args.get('protocol')
            # 根据domain参数获取域名
            domain = request.args.get('domain')

            proxy = self.proxy_pool.random(protocol=protocol, domain=domain, count=settings.AVAILABLE_IP_COUNT)

            # 如果有协议, 就返回带有协议代理IP和端口号
            if protocol:
                return '{}://{}:{}'.format(protocol, proxy.ip, proxy.port)
            else:
                # 如果没有协议就返回, 不带协议的IP和端口号
                return '{}:{}'.format(proxy.ip, proxy.port)

        @self.app.route('/proxies')
        def proxies():
            # 根据protocol参数获取协议
            protocol = request.args.get('protocol')
            # 根据domain参数获取域名
            domain = request.args.get('domain')

            proxies = self.proxy_pool.get_proxies(protocol=protocol, domain=domain, count=settings.AVAILABLE_IP_COUNT)
            lis = []
            for proxy in proxies:
                lis.append(proxy.__dict__)
            return json.dumps(lis)

        @self.app.route('/disable_domain')
        def disable_domain():
            # 获取IP地址
            ip = request.args.get('ip')
            # 获取不可用域名
            domain = request.args.get('domain')
            if ip is None:
                return '请传入ip参数'
            if domain is None:
                return '请传入domain参数'

            # 更新域名成功
            self.proxy_pool.disable_domain(ip=ip, domain=domain)
            return '该IP添加不可用域名成功'

    def run(self):
        self.app.run(host="0.0.0.0",port=6868)

    @classmethod
    def start(cls):
        proxy_api = cls()
        proxy_api.run()

if __name__ == '__main__':
    ProxyApi.start()
```

- `小结`:
    - 实现给爬虫提供高可用代理IP的接口
        1. 实现根据协议类型和域名, 提供随机的高可用代理IP的服务
        2. 实现根据协议类型和域名, 提供多个高可用代理IP的服务
        3. 实现给指定的IP上追加不可用域名的服务 