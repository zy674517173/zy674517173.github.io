from time import sleep

from base.web_base import WebBase
import page

class PageMpArticle(WebBase):

    # 1. 点击内容管理
    def page_click_content_manage(self):
        sleep(1)
        self.base_click(page.mp_content_manager)

    # 2. 点击发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 3. 点击输入标题
    def page_input_title(self, title):
        sleep(1)
        self.base_input(page.mp_title, title)

    # 4. 点击输入内容
    def page_input_content(self, content):
        # 1. 切换 iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        sleep(1)
        # 2. 输入内容
        self.base_input(page.mp_content, content)
        # 3. 回到默认目录
        self.driver.switch_to.default_content()

    # 5. 封面
    def page_click_cover(self):
        sleep(1)
        self.base_click(page.mp_cover)

    # 6. 频道
    def page_click_channel(self):
        # 调用 webBase封装方法
        self.web_base_click_element(placeholder_text="请选择", click_text="数据库")
        pass

    # 7. 发布按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 8. 获取发布信息
    def page_get_info(self):
        t = self.base_get_text(page.mp_result)
        return t

    # 9. 组合发布文章方法
    def page_mp_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()


