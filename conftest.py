import pytest
from selenium import webdriver


from PageObjects.login_page_xcfb import LoginPageXcfb
from TestDatas import common_datas as CD
from Common.logger import Logger
import time


logger = Logger(__name__).getlog()
driver = None
#声明它是一个fixture
@pytest.fixture(scope="class")
def access_web1():
    global driver
    #前置操作
    print("=====测试用例执行之前，setUpClass，整个测试类只执行一次")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg = LoginPageXcfb(driver)
    yield (driver,lg)  #分割线； #后面接返回值
    #后置操作
    print("=====测试用例执行之后，tearDownClass，整个测试类只执行一次")
    driver.quit()

@pytest.fixture()
def refresh_page1():
    global driver
    #前置操作
    yield
    #后置操作
    logger.info("======每一个用例后置：刷新当前页面======")
    driver.refresh()
    time.sleep(0.5)












