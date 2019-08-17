import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_DIR = os.path.join(BASE_DIR, "configs")

CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "config.conf")

LOG_DIR = os.path.join(BASE_DIR, "logs")

DATA_DIR = os.path.join(BASE_DIR, "datas")

DATA_DIR_FILE_PATH = os.path.join(DATA_DIR, "cases.xlsx")

REPORT_DIR = os.path.join(BASE_DIR, "reports")

CASES_DIR = os.path.join(BASE_DIR, "cases")

USER_CONFIG_FILEME = os.path.join(CONFIG_DIR, "user.conf")
pass