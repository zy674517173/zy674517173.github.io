import allure
from selenium.webdriver.support.ui import WebDriverWait
from tools.get_log import GetLog
from time import sleep

log = GetLog.get_logger()

class Base:

    # 初始化
    def __init__(self, driver):
        '''解决driver'''
        log.info("正在初始化Driver:{}".format(driver))
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认 30s
        :param poll: 查找元素频率 默认 0.5
        :return:  元素
        """
        # 元素定位 -- 元素等待(显式等待)  self.driver.find_element(*loc)
        # 显式等待的优点：1、返回元素    2、可以修改查找的频率
        # loc 为元组或列表（*loc为解包 == loc[0], loc[1]）
        log.info("元素{}正在进行定位操作...".format(loc))
        element = WebDriverWait(self.driver,
                                timeout=timeout,
                                poll_frequency=poll).until(lambda d:d.find_element(*loc))
        return element


    # 输入 方法封装
    def base_input(self, loc, value):
        """
        指定元素完成输入操作
        :param loc: 元素定位信息
        :param value: 输入内容
        :return: 无
        """
        # 1、获取元素
        el = self.base_find(loc)
        # 2、清空操作
        log.info("元素{}正在进行清空操作...".format(loc))

        # 检查元素是否为输入框或文本域
        if el.tag_name in ['input', 'textarea']:
            try:
                # 2. 使用JavaScript清空输入框内容
                self.driver.execute_script("arguments[0].value = '';", el)
                log.info(f"通过JavaScript对元素{loc}清空")
            except Exception as e:
                log.error(f"使用JavaScript清空元素{loc}失败: {str(e)}")

        # el.clear()
        # 3、输入操作
        log.info("元素{}正在进行输入操作,内容是{}...".format(loc, value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        :return: 无
        """
        # 获取元素并点击
        log.info("元素{}正在进行点击操作...".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 获取文本
        """
        t = self.base_find(loc).text
        log.info("元素{}正在进行获取文本操作,文本是:{}...".format(loc, t))
        return t

    # 截图
    def base_get_img(self):
        log.error("断言出错，正在执行截图操作！")
        # 1.调用截图方法
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将错误图片写入allure报告")
        # 2.调用图片写入报告方法
        self.__base_write_img()


    # 将图片写入报告方法（私用）
    def __base_write_img(self):
        # 1. 获取图片文件流
        with open("./image/err.png", "rb") as f:
            # 2. 调用allure.attach附加方法
            allure.attach("错误原因", f.read(), allure.attachment_type.PNG)










