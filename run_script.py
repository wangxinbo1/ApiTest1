import unittest
import time
import os
from scripts.constant import REPORT_DIR,CASES_DIR,USER_CONFIG_FILEME
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_user import generate_users_config
#第一种方法：
# # 定义一个测试套件
# suite1 = unittest.TestSuite()
#
# # 定义一个加载器，用来加载模块用例到测试套件
# loader = unittest.TestLoader()
# suite1.addTest(loader.loadTestsFromModule(test_divide))
# suite1.addTest(loader.loadTestsFromModule(test_substruction))
# # 定义一个执行器对象
# run1 = unittest.TextTestRunner()
# run1.run(suite1)

if not os.path.exists(USER_CONFIG_FILEME):
    generate_users_config()
from datetime import datetime

#datetime.now()
# suite2 = unittest.TestSuite()
#
# # 第二种方法：
# suite2.addTest(loader.loadTestsFromModule(test_divide))
suite2 = unittest.defaultTestLoader.discover(start_dir=CASES_DIR, pattern="test*.py")
# run2 = unittest.TextTestRunner()
# run2.run(suite2)
current_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
report_filename = os.path.join(REPORT_DIR, (str(current_time) + "report.html"))
with open(report_filename, "wb") as one_file:
    run2 = HTMLTestRunner(stream=one_file,
                          title="柠檬班的第一份测试报告",
                          description="联系html报告生成",
                          verbosity=1,
                          tester="老王")
    run2.run(suite2)

# print(time.time())
# print(time.localtime())
# a=time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
# print(type(a))

