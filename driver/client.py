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
            chrome_options.add_argument('disable-infobars') #设置不弹出自动化提示
            # chrome_options.add_argument('--headless') #后台运行
            # chrome_options.add_argument('--disable-gpu')
            # chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument('--window-size=1200,600')
            # driver = webdriver.Chrome(chrome_options=chrome_options)
            cls.driver = webdriver.Chrome(config.driver_dir, options=chrome_options)
        elif browser == "IE":
            cls.driver = webdriver.Ie()
        # self.driver.set_window_size(1920, 1080)  # 分辨率
        # self.driver.maximize_window()#最大化
        cls.driver.get(baseURL)
        cls.driver.implicitly_wait(10)
        return cls.driver



