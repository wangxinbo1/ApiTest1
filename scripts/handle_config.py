from configparser import ConfigParser
from scripts.constant import CONFIG_FILE_PATH
class DoConfigFile():

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    @staticmethod
    def do_write(datas, filename):
        other_config = ConfigParser()
        for i in datas:
            other_config[i] = datas[i]
        with open(filename, "w") as f:
            other_config.write(f)


config_read_file = DoConfigFile(CONFIG_FILE_PATH)

if __name__ == "__main__":
    config1 = DoConfigFile("config1.ini")
    # config1.get_value("msg", "name")
    datas = {
        "msg": {
            "name": "laowang",
            "age": '20'
        }
    }
    config1.do_write(datas, "config1.ini")
    pass

