import unittest
import os
from libs.ddt import ddt, data
from scripts.handle_excel import HandleExcel
from scripts.handle_config import config_read_file
from scripts.constant import DATA_DIR
from scripts.handle_requests import HandleRequest
from scripts.handle_log import logger
from scripts.handle_context import HandleContext

# 读取excel
do_excel = HandleExcel(os.path.join(DATA_DIR, config_read_file.get_value("excel", "case_excel")), "recharge")
all_cases = do_excel.get_cases()


@ddt
class TestRecharge(unittest.TestCase):
    """
    定义一个测试充值的测试类
    """

    @classmethod
    def setUpClass(cls):
        cls.resp = HandleRequest()
        logger.info("******************************************************")
        logger.info("{0}".format("开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        cls.resp.close()
        logger.info("{0}".format("执行用例完成"))
        logger.info("******************************************************")

    @data(*all_cases)
    def test_user_login(self, one_case):
        logger.info("正在执行第{0}条用例:{1}".format(one_case["case_id"], one_case["title"]))

        url_new = config_read_file.get_value("api", "url") + one_case["url"]
        new_data = HandleContext.borrow_context(one_case["data"])
        logger.info("\n请求url为{0}\ndata为{1}".format(url_new, new_data))
        register = self.resp.sendRequests(method=one_case["method"], url=url_new, data=eval(new_data))  # 返回登录响应对象

        logger.info("\n响应数据为{1}".format(url_new, register.text))
        try:
            self.assertIn(str(one_case["expected"]), register.text, msg=one_case["title"])
            logger.info("\'{0}\'用例执行成功".format(one_case["title"]))
            result = "True"
        except AssertionError as err:
            logger.error("{0}用例执行失败，错误信息为: {1}".format(one_case["title"], err))
            result="False"
            raise err
        finally:
            logger.info("写入结果开始")
            do_excel.write_result(row=one_case["case_id"] + 1, column=8, result=result)
            do_excel.write_result(row=one_case["case_id"] + 1, column=7, result=register.text)
            logger.info("写入结果结束")


if __name__ == "__main__":
    unittest.main()




