import unittest
from loguru import logger
from apis.user_manager_api import UserManagerApi
from data.user_manager_data import user_manager_data
class TestUserManagerCase(unittest.TestCase):
    user_id = 235
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = UserManagerApi()

    # 实现添加测试用例
    def test01_add_user(self):
        # 定义数据
        # 调用接口
        result = self.api.add_manager(user_manager_data["username"],user_manager_data["password"])
        logger.info("增加管理员返回数据{}".format(result))
        TestUserManagerCase.user_id = result.get("data").get("id")
        # 断言
        self.assertEqual(0,result.get("errno"))

    # 实现编辑测试用例
    def test02_update_user(self):
        result = self.api.update_manager(TestUserManagerCase.user_id,user_manager_data["new_name"],user_manager_data["password"])
        logger.info("编辑管理员返回数据{}".format(result))
        self.assertEqual(0,result.get('errno'))

    # 实现查询测试用例
    def test03_search_user(self):
        result = self.api.search_manager()
        logger.info("查询管理员返回数据{}".format(result))
        self.assertEqual(20,result.get("data").get('limit'))

    # 实现删除测试用例
    def test04_delete_user(self):
        result = self.api.delete_manager(TestUserManagerCase.user_id,user_manager_data["new_name"],user_manager_data["password"])
        logger.info("删除管理员返回数据{}".format(result))
        self.assertEqual(0,result.get('errno'))