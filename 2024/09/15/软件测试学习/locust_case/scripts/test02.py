
from locust import HttpUser, SequentialTaskSet


''' 1. 定义任务 '''
# 1. 登陆
def login(session):
    # 请求post方法
    r = session.client.post(url="/bms/login", data={"username":"admin","password":"123456"})
    # 查看登陆结果 json
    print(r.json)

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

''' 2. 定义任务集 '''
class TaskTest(SequentialTaskSet):
    # 复写Tasks属性
    tasks = [login, index, user, logout]

''' 3. 定义用户类 '''
class UserRun(HttpUser):
    # 复写 taskset
    taskset = TaskTest

    # 定义 host
    host = "http://182.92.81.159:1880"