
from locust import HttpUser, SequentialTaskSet


''' 1. 定义任务 '''
# 1. 登陆
def login(session):
    # 请求post方法
    r = session.client.post(url="/bms/login", data={"username":"admin","password":"123456"})
    # 查看登陆结果 json
    print(r.json)
    print("正在调用登陆方法。。。")

# 2. 打开首页
def index(session):
    # 调用get方法
    r = session.client.get(url="/bms/index")
    # 查看结果 text 方法解析
    print(r.text)

# 3. 查询用户信息
def user(session):
    # 调用get方法
    r = session.client.get(url="/bms/user")
    # 查看结果
    print(r.text)

# 4. 退出登陆
def logout(session):
    # 调用post方法
    r = session.client.post(url="/bms/logout")
    # 查看结果
    print(r.json)
    print("正在调用退出登陆方法。。。")

''' 2. 定义任务集 '''
class TaskTest(SequentialTaskSet):
    # 复写Tasks属性
    # tasks = [index, user]
    tasks = {index:10, user:1}

    # 初始化执行方法
    def onstart(self):
        login(self)

    # 结束执行方法
    def on_start(self):
        logout(self)

''' 3. 定义用户类 '''
class UserRun(HttpUser):
    # 复写 taskset
    taskset = TaskTest

    # 定义 host
    host = "http://182.92.81.159:1880"

    # 最小延迟时间 毫秒
    min_wait= 1000
    # 最大延迟时间
    max_wait = 3000
    # 权重
    weight = 10