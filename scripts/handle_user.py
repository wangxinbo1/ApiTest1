from scripts.handle_mysql import HandleSql
from scripts.handle_requests import HandleRequest
from scripts.handle_config import config_read_file
from scripts.constant import USER_CONFIG_FILEME

def create_new_user(username, pwd="123456"):
    """
    创建用户信息
    :param renamne:
    :param passwd:
    :return:
    """
    handle_mysql = HandleSql()
    send_resquest = HandleRequest()
    url_new = config_read_file.get_value("api", "url") + "/member/register"
    sql = "select * from member where MobilePhone = %s"
    while True:
        mobile_phone = handle_mysql.create_not_exists_phone()
        data = {"mobilephone": mobile_phone, "pwd": pwd, "regname": username}
        send_resquest.sendRequests("post", url_new, data=data)
        result = handle_mysql.run_sql(sql,args=(mobile_phone, ))
        if result:
            user_id = result["Id"]
            break

    user_dict = {
        username :{
            "Id": user_id,
            "rename": username,
            "mobile_phone":mobile_phone,
            "pwd": pwd
        }

    }

    send_resquest.close()
    handle_mysql.close_mysql()
    return user_dict

def generate_users_config():
    user_datas_dict={}
    user_datas_dict.update(create_new_user("admin_user_personal"))
    user_datas_dict.update(create_new_user("invest_user_personal"))
    user_datas_dict.update(create_new_user("borrow_user_personal"))
    config_read_file.do_write(user_datas_dict, USER_CONFIG_FILEME)

if __name__=="__main__":
    generate_users_config()