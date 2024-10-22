

from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml
from page.page_in import PageIn
from tools.get_log import GetLog

import pytest
import page

log = GetLog.get_logger()

class TestMPLogin:
    # 初始化
    def setup_class(self):
        # 1.获取 driver 对象
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.通过统一入口类获取 PageMpLogin 对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭 driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))

    def test_mp_login(self, username, code, expect):
        # 调用登陆业务方法
        self.mp.page_mp_login(username, code)
        try:
            # 断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error("断言出错：错误信息：{}".format(e))
            # 输出错误信息
            print("错误原因：", e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise















