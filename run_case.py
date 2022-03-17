from apis.base import Base
from setting import  LOGIN_DATA,FILE_NAME
from HTMLTestRunner import HTMLTestRunner
import unittest

if __name__ == '__main__':
    Base().login(LOGIN_DATA['username'], LOGIN_DATA['password'])
    suite = unittest.TestLoader().discover('./cases','test*.py')

    with open(FILE_NAME,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)

