from page.page_in import PageIn
from tools.get_driver import GetDriver
import page


class TestMpArticle:
    # 1. 初始化
    def setup_class(self):
        # 1. 获取 driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 获取统一入口类
        self.page_in = PageIn(driver)
        # 3. 获取 PageMpLogin 对象 并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4. 获取 PageMpArticle 页面对象
        self.article = self.page_in.page_get_PageMpAriticle()


    # 2. 结束
    def teardown_class(self):
        # 关闭 driver
        GetDriver.quit_web_driver()

    # 3.测试发布文章方法
    def test_mp_article(self, title="test001-bj001", content="今晚吃汤饭！"):
        # 调用发布文章业务方法
        self.article.page_mp_article(title, content)
        # 查看断言信息
        print("发布文章的结果为：", self.article.page_get_info())

