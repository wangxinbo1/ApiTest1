import pymysql
import random
from scripts.handle_config import config_read_file


class HandleSql:
    """
    处理封装mysql
    """

    def __init__(self):
        self.conn = pymysql.connect(host=config_read_file.get_value("sql", "host"),
                                    user=config_read_file.get_value("sql", "user"),
                                    password=config_read_file.get_value("sql", "password"),
                                    db=config_read_file.get_value("sql", "db"),
                                    port=config_read_file.get_int("sql", "port"),
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def close_mysql(self):
        """
        关闭sql连接
        :return:
        """
        self.cursor.close()
        self.conn.close()

    def run_sql(self, sql, args=None, is_more=False):
        """
        执行sql语句
        :param sql:
        :param args:
        :param is_more:
        :return:
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    @staticmethod
    def random_generate_phone():
        start_phone = ['151', '134', '187']
        result_phone = random.choice(start_phone) + ''.join(random.sample('0123456789', 8))
        return result_phone

    def phone_is_exists(self, phone):
        result = False
        sql = "select * from member where MobilePhone = %s"
        if self.run_sql(sql,args=(phone,)) is not None:
            result = True
        return result

    def create_not_exists_phone(self):
        while True:
            phone = self.random_generate_phone()
            if not self.phone_is_exists(phone):
                return phone



if __name__=="__main__":
    do_sql = HandleSql()
    sql = "select * from member where MobilePhone = %s"
    result = do_sql.run_sql(sql, args=(15921919560,), is_more=True)
    pass
    # print(f"{result}\n{type(result)}")
    # print(do_sql.random_generate_phone())
    # print(do_sql.phone_is_exists('15921919560'))
