import requests

class HandleRequest():
    """
    定义一个封装类
    """
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }

    def __init__(self):
        self.res = requests.Session()

    def close(self):
        self.res.close()

    def sendRequests(self, method, url, data, headers=None, is_json=False):
        if method.lower() == "post":
            if is_json:
                return self.res.post(url, json=data, headers=headers, proxies=None)
            else:
                return self.res.post(url, data=data, headers=headers, proxies=None)
        elif method.lower() == "get":
            return self.res.get(url, params=data, headers=headers, proxies=None)
        else:
            self.res = None
            print("输入请求不支持")


if __name__ == "__main__":
    url = "http://tj.lemonban.com/futureloan/mvc/api/member/register"
    url1 = "http://tj.lemonban.com/futureloan/mvc/api/member/login"
    url2 = "http://tj.lemonban.com/futureloan/mvc/api/member/recharge"
    data = {"mobilephone": "18710797197","pwd": "123456", "regname": "wangxin"}
    data1 = '{"mobilephone": "18710797194","pwd": "123456"}'

    data2 = {"mobilephone": "18710797194",
             "amount": 1000
             }
    # reg = requests.get(url, params=data)
    resp = HandleRequest()
    # register = resp.sendRequests("get", url, data)  # 返回注册响应对象

    login = resp.sendRequests("post", url1, data1)  # 返回登录响应对象
    print(login.text)
 #   recharge = resp.sendRequests("post", url2, data2)  # 返回充值响应对象
    pass
