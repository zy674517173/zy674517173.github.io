
from selenium.webdriver.common.by import By

# 元素配置信息统一存放管理（__init__.py）
# 能使用 CSS 选择器定位， 不适用 xpath 定位
"""以下数据为自媒体、后台管理 url"""
# 自媒体 url
url_mp = "http://pc-toutiao-python.itheima.net/#/login"
# 后台管理
url_mis = ""

"""以下数据为自媒体模块配置数据"""

# 用户名
mp_username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')

# 验证码
mp_code = (By.CSS_SELECTOR, '[placeholder="验证码"]')

# 登陆按钮
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')

# 昵称
mp_nickname = (By.CSS_SELECTOR, '.user-name')

# 内容管理      XPATH 查找
mp_content_manager = By.XPATH, "//span[text()='内容管理']/.."

# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(), '发布文章')]"

# 文章标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"

# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"

# 文章内容   定位到body， 勿定位到p标题
mp_content = By.CSS_SELECTOR, "#tinymce"

# 封面
mp_cover = By.XPATH, "//*[text()='自动']"         #  选择自动方法

# 发表
mp_submit = By.XPATH, "//*[text()='发表']/.."

# 结果
mp_result = By.XPATH, "//*[contains(text(), '新增文章成功')]"