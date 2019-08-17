import re
from scripts.handle_mysql import HandleSql
from scripts.handle_config import DoConfigFile
from scripts.constant import USER_CONFIG_FILEME

class HandleContext:
    """
    处理参数化
    """
    not_register_phone = r"\${not_register_phone}"
    invest_phone = r"\${invest_phone}"
    borrow_phone = r"\${borrow_phone}"
    admin_phone = r"\${admin_phone}"

    handle_user_config = DoConfigFile(USER_CONFIG_FILEME)

    @classmethod
    def not_existed_phone_context(cls, data):
        if re.search(cls.not_register_phone, data):
            do_sql = HandleSql()
            data = re.sub(cls.not_register_phone, do_sql.create_not_exists_phone(), data)
            do_sql.close_mysql()
        return data

    @classmethod
    def invest_context(cls, data):
        invest_user_phone = cls.handle_user_config.get_value("invest_user_personal", "mobile_phone")
        data = re.sub(cls.invest_phone, invest_user_phone, data)
        return data

    @classmethod
    def borrow_context(cls, data):
        borrow_user_phone = cls.handle_user_config.get_value("borrow_user_personal", "mobile_phone")
        data = re.sub(cls.borrow_phone, borrow_user_phone, data)
        return data

    @classmethod
    def admin_context(cls, data):
        admin_user_phone = cls.handle_user_config.get_value("admin_user_personal", "mobile_phone")
        data = re.sub(cls.admin_phone, admin_user_phone, data)
        return data

    @classmethod
    def reginster_paramization(cls, data):
        data = cls.not_existed_phone_context(data)
        data = cls.invest_context(data)
        return data

    @classmethod
    def recharge_paramization(cls, data):
        data = cls.borrow_context(data)
        return data

    @classmethod
    def add_paramization(cls, data):
        data = cls.admin_context(data)
        return data


if __name__=="__main__":
    data = '{"wanng":"${not_register_phone}"}'
    data1 = {'{"wanng":"${invest_phone}"}'}
    do_context = HandleContext()
    print(do_context.reginster_paramization(data))
    pass