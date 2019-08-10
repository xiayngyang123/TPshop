"""对APPium进行二次封装"""
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
def open_mobile():
    """打开手机"""
    desired_caps={}
    #指定系统
    desired_caps["platformName"]="android"
    #指定版本
    desired_caps["platformVersion"]="5.1.1"
    #设备名称
    desired_caps["deviceName"]="TPshop"
    #启动APP包名
    desired_caps["appPackage"]="com.tpshop.malls"
    #APP启动名
    desired_caps["appActivity"]=".SPMainActivity"
    # 启用Unicode输入法，设置为true可以输入中文字符，默认为false
    desired_caps['unicodeKeyboard'] = True
    #如果单独使用，将会被忽略，默认值`false`
    desired_caps['resetKeyboard'] = True
    #不重置应用
    desired_caps["noReset"] = True
    # 添加一个新的参数
    desired_caps["automationName"] = "Uiautomator2"
    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    return driver
class Base:

    def __init__(self,driver):
        self.driver=driver
        data=self.driver.get_window_size()
        self.x=data["width"]
        self.y=data["height"]
    def find_element(self,locator,timeout=5):
        """
        定位单个元素
        :param locator: 定位器
        :param timeout: 最大等待时间
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout,0.1).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")

    def find_elements(self,locator,timeout = 5):
        """
        定位一组元素,返回元素
        :param locator: 定位器,元祖("id","id属性值")
        :param timeout: 最大等待时间
        :return: elements
        """
        elements = WebDriverWait(self.driver,timeout,0.1).until(EC.presence_of_all_elements_located(locator))
        return elements
    def element_click(self,element):
            """点击"""
            element.click()
    def click(self, locator, timeout=5):
        """
        点击单个元素
        :param locator:定位器
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        element.click()
    def click_group(self,locator,timeout=5):
        """点击一组元素"""
        elements=self.find_elements(locator,timeout)
        for element in elements:
            element.click()

    def element_focus(self,locator,timeout=5):
        """聚焦元素"""
        while True:
            try:
                element=self.find_element(locator,timeout)
                element.click()
                break
            except:
                self.swipe_up()
    def send_keys(self, locator, text, timeout=5):
        """
        输入
        :param locator:
        :param timeout:
        :param text:输入的内容
        :return:
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=5):
        """
        判断文本是否在元素中,如果存在,返回True,如果不存在,返回False
        :param locator: 定位器
        :param text: 将要判断的文本--已知文本
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout, 0.1).until(EC.text_to_be_present_in_element(locator, text))
        except:
            print(f"{locator}元素没找到")
            return False
        else:
            return result

    def browser_back(self):
        """后退"""
        self.driver.back()

    def browser_refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def swipe_up(self):
        """向上滑动"""
        self.driver.swipe(self.x * 0.2, self.y * 0.9, self.x * 0.2, self.y * 0.1, duration=3000)

    def swipe_down(self):
        """向下滑动"""
        self.driver.swipe(self.x * 0.2, self.y * 0.1, self.x * 0.2, self.y * 0.9, duration=3000)

    def swipe_left(self):
        """向左滑动"""
        self.driver.swipe(self.x * 0.1, self.y * 0.2, self.x * 0.8, self.y * 0.2, duration=3000)

    def swipe_right(self):
        """向右滑动"""
        self.driver.swipe(self.x * 0.8, self.y * 0.2, self.x * 0.1, self.y * 0.2, duration=3000)

    def tap(self,x,y):
        """
        TouchAction里面tap点击
        :param locator: 定位器
        :return:      ([12,13],)
        """

        TouchAction(self.driver).tap(x=x,y=y).perform()
    def press(self,locator):
        """TouchAction里面press点击"""
        element = self.find_element(locator)
        TouchAction(self.driver).press(element).release().perform()
    def random_index(self):
        """随机点击商品"""
        index=random.randint(0,6)
        return index

    def all_toast(self,text,timeout=10):
        """
        获取toast
        :param text: toast文本(可以模糊查询)
        :param timeout:
        :return:
        """
        locator = ("xpath", f"//*[contains(@text,'{text}')]")
        try:

            element = WebDriverWait(self.driver, timeout,0.1).until(EC.presence_of_element_located(locator))
            toast_text=element.text
            return toast_text
        except TimeoutError:
            print("toast没找到")

if __name__ == '__main__':
    print(Base)