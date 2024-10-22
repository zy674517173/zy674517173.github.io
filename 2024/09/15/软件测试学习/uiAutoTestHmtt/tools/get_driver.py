'''
1. 类级别操作
类方法是对类本身进行操作的，而不是对类的某个实例进行操作。例如，可以使用类方法来修改类级别的属性或执行涉及类整体的操作。

2. 工厂方法
类方法通常被用作工厂方法。工厂方法允许通过不同的输入来创建类的实例，而不是通过通常的构造函数。比如，根据不同的条件创建对象的不同实例。

3. 访问类属性
类方法可以访问和修改类属性（即共享给所有实例的变量），而实例方法则只能访问实例属性。通过类方法，可以统一对整个类的状态进行操作。

4. 继承中的应用
类方法在继承时非常有用，它们可以在继承的子类中调用，并且会自动绑定到子类，而不是基类。这使得它们比静态方法更灵活，能够根据子类的需求来执行操作。

'''

from selenium import webdriver

class GetDriver:
    # 1. 声明 driver 变量
    __web_driver = None     # 编程私有受保护的变量

    # 2. 获取 driver 方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断 driver 是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 浏览器最大化
            cls.__web_driver.maximize_window()
            # 打开 url
            cls.__web_driver.get(url)

        # 返回 driver
        return cls.__web_driver

    # 3. 退出driver 方法
    @classmethod
    def quit_web_driver(cls):
        # 判断 driver 不为空
        if cls.__web_driver is not None:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作  重点
            cls.__web_driver = None











