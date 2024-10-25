
from locust import HttpUser, SequentialTaskSet, task

"""
    目标：locust分布式
    角色：主机
        1、主机（控制机）   --master
        2、丛书主机（执行机）     --slave --master-host=主机IP地址
    从属主机必须依赖重点：
        1. 必须有python和locust环境
        2. 必须有主机脚本的副本
"""


''' 2. 定义任务集 '''
class TaskTest(SequentialTaskSet):
    # 复写Tasks属性
    # tasks = [index, user]
    # tasks = {index:10, user:1}

    # 1. 登陆
    def login(self):
        # 请求post方法
        r = self.client.post(url="/bms/login", data={"username": "admin", "password": "123456"})
        # 查看登陆结果 json
        print(r.json)
        print("正在调用登陆方法。。。")

    # 2. 打开首页
    @task(10)
    def index(self):
        # 调用get方法
        r = self.client.get(url="/bms/index")
        # 查看结果 text 方法解析
        print(r.text)

    # 3. 查询用户信息
    @task(1)
    def user(self):
        # 调用get方法
        r = self.client.get(url="/bms/user")
        # 查看结果
        print(r.text)

    # 4. 退出登陆
    def logout(self):
        # 调用post方法
        r = self.client.post(url="/bms/logout")
        # 查看结果
        print(r.json)
        print("正在调用退出登陆方法。。。")

    # 初始化执行方法
    def onstart(self):
        self.login()

    # 结束执行方法
    def on_start(self):
        self.logout()

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