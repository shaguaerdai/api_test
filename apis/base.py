import requests
from setting import BASE_URL
from cacheout import Cache
from loguru import logger
cache = Cache()
# 定义类
class Base(object):

    # 实现url的方法
    def get_url(self,path,params=None):
        '''

        :param path: 接口路径
        :param params: 查询字符串
        :return: 返回url
        '''
        if params:
            return BASE_URL + path + '?' + params
        return BASE_URL + path

    # 实现get方法
    def get(self,url):
        '''

        :param url: url地址
        :param headers: 请求头
        :return: 响应体
        '''
        try:
            response = requests.get(url,headers=self.get_headers())
            result = response.json()
            return result
        except Exception as e:
            logger.error("请求get方法失败，错误信息{}",e)

    #实现 post方法
    def post(self,url,post_data):
        '''

        :param url: url地址
        :param headers: 请求头
        :return: 响应体
        '''
        try:
            response = requests.post(url=url,json=post_data,headers=self.get_headers())
            result = response.json()
            return result
        except Exception as e:
            logger.error("请求post方法失败，错误信息{}", e)


    # 实现登录方法
    def login(self,username,password):
        '''

        :param username:
        :param password:
        :return:
        '''
        login_path = '/admin/auth/login'
        login_url = self.get_url(login_path)
        login_data = {"username":username,"password":password}
        result = self.post(login_url,login_data)
        try:
            if result.get("errno") == 0:
                token = result.get("data").get("token")
                cache.set("token",token)
                logger.info("登陆成功!")
            else:
                logger.info("登录失败，失败原因：{}".format(result))
        except Exception as e:
            logger.error("请求登录接口失败,错误信息{}".format(e))

    # 获取请求头
    def get_headers(self):
        '''

        :return: 请求头
        '''
        headers = {"Content-Type":"application/json"}
        token = cache.get("token")
        if token:
            headers.update({"X-Litemall-Admin-Token":token})
            logger.info("加了token的请求头为{}".format(headers))
        return headers








if __name__ == '__main__':
    b = Base()
    print(b.get_url("/admin/auth/login"))
    print(b.get_url("/admin/auth/login","page=1&limit=20&sort=add_time&order=desc"))
    print(b.get("http://www.weather.com.cn/data/sk/101010100.html"))