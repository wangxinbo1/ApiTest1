import unittest
import os
from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import config_read_file
from scripts.constant import DATA_DIR,USER_CONFIG_FILEME
from scripts.handle_requests import HandleRequest
from scripts.handle_log import logger
from scripts.handle_user import generate_users_config

# 读取excel
he = HandleExcel(os.path.join(DATA_DIR, config_read_file.get_value("excel", "case_excel")), "login")
all_cases = he.get_cases()

if not os.path.exists(USER_CONFIG_FILEME):
    generate_users_config()
@ddt
class TestSubstruction(unittest.TestCase):
    """
    定义一个测试投资接口的测试类
    """

    @classmethod
    def setUpClass(cls):
        cls.resp = HandleRequest()
        logger.info("******************************************************")
        logger.info("{:=^40s}".format("开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        cls.resp.close()
        logger.info("用例执行完成\n")
        logger.info("******************************************************")


    @data(*all_cases)
    def test_user_login(self, one_case):

        url_new = config_read_file.get_value("api","url") + one_case["url"]

        login = self.resp.sendRequests(method=one_case["method"], url=url_new, data=eval(one_case["data"]))  # 返回登录响应对象
        logger.info("\n请求url为{0}\ndata为{1}".format(url_new,login.text))
        try:
            self.assertEqual(one_case["expected"], login.text, msg=one_case["title"])
            logger.info("\'{0}\'用例执行成功".format(one_case["title"]))
        except AssertionError as err:
            logger.error("{0}用例执行失败，错误信息为: {1}".format(one_case["title"], err))
            raise err


if __name__ == "__main__":
    unittest.main()




