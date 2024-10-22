from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin

# 统一入口类

class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取 PageMpLogin 对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取 PageMpArticle 对象
    def page_get_PageMpAriticle(self):
        return PageMpArticle(self.driver)