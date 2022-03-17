from apis.base import Base
from loguru import logger



class UserManagerApi(Base):

    def __init__(self):
        self.add_path = "/admin/admin/create"
        self.update_path = "/admin/admin/update"
        self.delete_path = "/admin/admin/delete"
        self.search_path = "/admin/admin/list?page=1&limit=20&sort=add_time&order=desc"

    # 增加管理员
    def add_manager(self,username,password,**kwargs):
        add_url = self.get_url(self.add_path)
        add_data = {"username":username,"password":password}
        if kwargs:
            add_data.update(**kwargs)
        logger.info("增加管理员请求体为{}".format(add_data))
        return self.post(add_url,add_data)

    # 编辑管理员
    def update_manager(self,user_id,username,password,**kwargs):
        update_url = self.get_url(self.update_path)
        update_data = {"id":user_id,"username": username,"password":password}
        if kwargs:
            update_data.update(**kwargs)
        logger.info("编辑管理员请求体为：{}".format(update_data))
        return self.post(update_url, update_data)

    # 查询管理员
    def search_manager(self):
        search_url = self.get_url(self.search_path)
        return self.get(search_url)

    # 删除管理员
    def delete_manager(self,user_id,username,password,**kwargs):
        delete_url = self.get_url(self.update_path)
        delete_data = {"id": user_id,"username":username,"password":password}
        if kwargs:
            delete_data.update(**kwargs)
        logger.info("删除管理员请求体为：{}".format(delete_data))
        return self.post(delete_url, delete_data)