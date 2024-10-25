from locust import HttpUser, SequentialTaskSet, task

# 1. 定义任务
''' 注： 普通函数，必须有一个形参'''
# 任务1 说话
def say(params):
    print("正在说话")

# 任务2 唱歌
def sing(params):
    print("正在唱歌")


# 2. 定义任务集
''' 注: 一个类必须继承 SequentialTaskSet 或 TaskSet，并使用 @task 注解来标记任务函数 '''
class TaskTest(SequentialTaskSet):

    tasks = [say, sing]

# 3. 定义用户类
''' 注： 一个类必须继承HttpLocust, 复写 task_set 参数，值为任务及类名称'''
class RunUser(HttpUser):
    # 复写 tasks 参数，值为任务集类名称
    taskset = [TaskTest]

    # 设置用户的等待时间（可选，可根据需要进行调整）
    wait_time = lambda self: 1