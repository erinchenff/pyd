import os
import re
import sys
import time
import yaml

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径

data_dir = os.path.join(base_dir, "data")  # data文件夹路径
conf_dir = os.path.join(base_dir, "conf")
cf_file = os.path.join(conf_dir, "config.yml")  # 环境配置文件路径
cf_file_local = os.path.join(conf_dir, "config_local.yml")  # 环境配置文件路径

# 日志路径
output_dir = os.path.join(base_dir, "output")
allure_dir = os.path.join(base_dir, "output", "allure")
log_time = time.strftime('%Y-%m-%d')
logs_log = os.path.join(output_dir, log_time + ".log")

# 截图路径
screenshot_dir = os.path.join(base_dir, "output", "screenshots/")


# case 路径
case_dir = os.path.join(base_dir, "testcase")
driver_dir = os.path.join(base_dir, "driver/chromedriver")


class Config():
    def __init__(self):
        with open(cf_file, encoding='utf8') as stream:
            configs = yaml.load(stream, Loader=yaml.FullLoader)

        with open(cf_file_local,encoding='utf8') as stream_local:
            configs_update = yaml.load(stream_local, Loader=yaml.FullLoader)

        self.configs = {**configs, **configs_update}

    @property
    def env(self):
        return self.configs.get("ENV")

    @property
    def browser(self):
        return self.configs.get("browser")

    @property
    def baseURL(self):
        '''
        首页
        :return:
        '''
        return self.get_section_option(self.env,"baseURL")

    @property
    def login_name_password(self):
        '''
        登陆账号密码
        :return:
        '''
        return (self.get_section_option(self.env,"login_iphone"), self.get_section_option(self.env,"login_password"))

    @property
    def input_price(self):
        '''
        输入的竞买额
        :return:
        '''
        return (self.configs.get('input_price'))

    @property
    def auction_interval_time(self):
        '''
        下一场间隔时间，单位秒
        :return:
        '''
        return (self.configs.get('auction_interval_time'))

    @property
    def auction_clear_time(self):
        '''
        购买后清场时间，单位秒
        :return:
        '''
        return (self.configs.get('auction_clear_time'))

    @property
    def set_url(self):
        '''
        '/dist/#/orderdetail?sn_local.yaml=${orderdetail}&status=live'
        集合URL
        :return:
        '''
        repl = self.configs[self.env]['orderdetail']
        set_relative_url = re.sub('\\${.*?}', repl, self.configs['set_url'])
        return self.baseURL + set_relative_url

    @property
    def access_token(self):
        return (self.configs.get('access_token'))


    def get_section_option(self, section, option):
        return self.configs.get(section).get(option)


cf = Config()
print("当前脚本运行环境为：%s" % cf.env)

if __name__ == '__main__':
    print(cf.login_name_password)
    print(cf.set_url)

    # 210510001202620171205134798225,0.01,0.0002,签署人（测试）新区开发两地公司
    # for i in range(100):
    #     str_my ="21051012211202990171205134798225" + str(i) + ",0.01,0.0002,签署人（测试）新区开发两地公司"
    #     print(str_my)
