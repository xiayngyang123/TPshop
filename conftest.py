from appium import webdriver
import pytest

@pytest.fixture()
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

