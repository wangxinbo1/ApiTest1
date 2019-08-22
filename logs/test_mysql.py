import pymysql
from scripts.handle_config import config_read_file
class HandleMysql:
    """
    定义一个数据库封装类
    """
    def __init__(self):

        self.conn = pymysql.connect(host=config_read_file.get_value("sql", "host"),
                                    user=config_read_file("sql", "user"),
                                    password=config_read_file("sql", "password"),
                                    db="test",
                                    charset="utf8",
                                    port=config_read_file("sql", "port"),
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursour = self.conn.cursor()

    def close(self):
        self.cursour.close()
        self.conn.close()

    def handle_sql(self, sql ,args=None, is_more=False):
        self.cursour.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursour.fetchone()
        else:
            return self.cursour.fetchall()

