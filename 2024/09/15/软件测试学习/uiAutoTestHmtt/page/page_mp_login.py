
from base.web_base import WebBase
import page
from time import sleep
from tools.get_log import GetLog

log = GetLog.get_logger()

# 根据用例业务操作步骤，将每步操作进行单独封装及业务组合调用方法
class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类里面输入的方法
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类里面输入的方法
        self.base_input(page.mp_code, code)


    # 点击登陆案例
    def page_click_login_btn(self):
        sleep(1)
        # 调用父类里面 点击
        self.base_click(page.mp_login_btn)


    # 获取昵称封装    -> 测试脚本曾断言使用
    def page_get_nickname(self):
        # 调用父类里面 获取文本 的方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法    ->测试脚本层调用
    def page_mp_login(self, username, code):
        log.info("正在对自媒体登陆业务方法，用户名：{} 密码：{}".format(username, code))
        # 调用相同页面的操作步骤，跨页面暂时不考虑
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法    -> 发布文章依赖使用
    def page_mp_login_success(self, username="12011111111", code="246810"):
        log.info("正在对自媒体登陆业务方法，用户名：{} 密码：{}".format(username, code))
        # 调用相同页面的操作步骤，跨页面暂时不考虑
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()