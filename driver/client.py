from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.remote.webdriver import WebDriver

from common.utils import get_logger
from conf import config

logg = get_logger(__name__)


class Client():
    driver: WebDriver

    @classmethod
    def open_browser(cls, browser, baseURL):
        if browser == "Firefox":
            cls.driver = webdriver.Firefox()
        elif browser == "Chrome":
            # 初始化driver
            chrome_options = Options()
            chrome_options.add_argument('disable-infobars')  # 设置不弹出自动化提示
            chrome_options.add_argument('--headless')  # 后台运行
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('window-size=2208x1242')  # 指定浏览器分辨率 ios目前占有率最高分辨率
            # cls.driver = webdriver.Chrome(executable_path="/Users/erin/PycharmProjects/pyd/driver/chromedriver")
            cls.driver = webdriver.Chrome(options= chrome_options)
            cls.driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub',
                                          desired_capabilities = DesiredCapabilities.CHROME,
                                          options=chrome_options,
                                          )
        elif browser == "IE":
            cls.driver = webdriver.Ie()

        cls.driver.get(baseURL)
        logg.info("当前脚本运行环境为：%s" % config.cf.env)
        logg.info("浏览器为：%s 已启动" % browser)
        # cls.driver.implicitly_wait(5)

        return cls.driver
