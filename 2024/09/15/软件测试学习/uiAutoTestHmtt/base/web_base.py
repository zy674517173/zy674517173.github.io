from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base

class WebBase(Base):
    '''以下为web项目专属方法'''

    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1. 点击元素框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)

        # 2. 暂停     必须暂停，因为这里是动态加载的复选框
        sleep(1)

        # 3. 点击包含显示文本的元素        文本只能使用 Xpath
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)


