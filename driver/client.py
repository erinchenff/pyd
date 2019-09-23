from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.remote.webdriver import WebDriver

from conf import config


class Client():
    driver: WebDriver

    @classmethod
    def open_browser(cls, browser, baseURL):
        if browser == "Firefox":
            cls.driver = webdriver.Firefox()
        elif browser == "Chrome":
            # 初始化driver
            chrome_options = Options()
            # chrome_options.add_argument('disable-infobars') # 设置不弹出自动化提示
            chrome_options.add_argument('--headless') # 后台运行
            chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('window-size=1397x877')  # 指定浏览器分辨率
            cls.driver = webdriver.Chrome(config.driver_dir, options=chrome_options)
        elif browser == "IE":
            cls.driver = webdriver.Ie()

        cls.driver.get(baseURL)
        cls.driver.implicitly_wait(10)

        return cls.driver



