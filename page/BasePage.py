from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.utils import get_logger
from driver.client import Client
from conf import config

import sys
import time

logg = get_logger(__name__)


class DialogException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class BasePage():

    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = Client.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return Client

    def get_text_to_be_present(self, locator, text, timeout=20) -> WebElement:
        '''
        定位元素，参数locator为元祖类型
        :param locator:
        :param eqc:
        :return:
        '''
        try:
            webelement = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text))
            logg.info('获取{}元素成功'.format(locator))
            return webelement
        except:
            logg.error("{}秒内没有定位到{}元素".format(timeout, locator))
            self.get_windows_img()

    def get_title_contains(self, text, timeout=2) -> WebElement:
        '''

        :param text:
        :param timeout:
        :return:
        '''

        try:
            res = WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text))
            logg.info('跳转{}页面成功'.format(text))
            return res
        except:
            logg.error("{}秒内没有跳转到{}页面".format(timeout, text))
            self.get_windows_img()

    def get_windows_img(self):
        try:
            # 寻找失败时自动截图至指定目录sreenshot，截图名称为调用方法名（测试用例名）+ 时间戳 + png后缀
            file_name = config.screenshot_dir + sys._getframe(1).f_code.co_name + time.strftime('%Y%m%d%H%M%S',
                                                                                                time.localtime(
                                                                                                    time.time())) + ".png"
            self.driver.get_screenshot_as_file(file_name)
            logg.info('Had take screenshots and save to folder:output/screenshots')
        except NameError as e:
            logg.info('Failed to take the screenshots!%s' % e)

    def find_element(self, *loc):
        """
        重封装的find方法，接受元组类型的参数，默认等待元素5秒，寻找失败时自动截图
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:元素对象webelement
        """
        try:
            webelement = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*loc))
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            logg.info('查找元素时，TimeoutException, NoSuchElementException')
            self.get_windows_img()

    def check_van_dialo(self):
        try:
            dialog_strs = ["本场竞拍已结束，请等待下一场\n确认",
                           "超出剩余可拍票面金额\n",
                           ]
            webelement = self.driver.find_element_by_xpath('//div[@role="dialog"]')
            logg.info("此页面有弹窗,webelement内容为：{}".format(webelement.text.split("\n")[0]))
            if webelement.text in dialog_strs:
                raise DialogException(webelement.text)
            else:
                logg.info("此页面有弹窗,webelement内容为：{}".format(webelement.text))
                self.get_windows_img()
        except NoSuchElementException:
            logg.info("当前页面无弹窗")
            return False

    def click_element(self, *loc):
        """
        重封装的click方法，将寻找和点击封装到一起，适用于点击次数不多的元素
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:None
        """
        try:
            webelement = self.find_element(*loc)
            webelement.click()
        except (TimeoutException, NoSuchElementException) as e:
            logg.info('详细错误:%s' % e.msg)

    def is_page_has_text(self, text):
        """
        判断当前页面是否存在指定的文字
        :param text:字符串类型，要判断是否存在的文字
        :return:布尔值，True代表存在，False代表不存在
        """
        nowtime = time.time()
        while self.driver.page_source.find(text) < 0:
            time.sleep(2)
            if time.time() - nowtime >= 30000:
                return False
        return True

    def switch_to_last_handles(self):
        """
        在打开的窗口里选择最后一个
        :return:None
        """
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

    def switch_to_another_hanles(self, now_handle):
        """
        只适用于打开两个窗口的情况，传入现在的窗口句柄后，选择另一个窗口
        :param now_handle:现在的窗口句柄
        :return:
        """
        # 得到当前开启的所有窗口的句柄
        all_handles = self.driver.window_handles
        # 获取到与当前窗口不一样的窗口
        for handle in all_handles:
            if handle != now_handle:
                self.driver.switch_to.window(handle)

    def clear_and_sendkeys(self, sendtexts, *loc):
        """
        先清除当前文本框内的文字再输入新的文字的方法
        :param sendtexts:要输入的新的文字
        :param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:None
        """
        try:
            webelement = self.find_element(*loc)
            webelement.clear()
            webelement.send_keys(sendtexts)
        except (TimeoutException, NoSuchElementException) as e:
            logg.info('详细错误 :%s' % e.msg)

    @classmethod
    def driver_quit(cls):
        logg.info('浏览器quit')
        cls.getDriver().quit()
