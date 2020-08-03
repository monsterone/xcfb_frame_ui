



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.indexpage_locators_xcfb import IndexPageLocatorXcfb as IL
from Common.basepage import BasePage


class IndexPageXcfb(BasePage):


    #断言用户名是否存在
    def isExist_logout_ele(self):
        #如果存在就返回True,如果不存在，就返回False
        try:
            doc = "首页页面_断言登录"
            self.wait_eleVisible(IL.index_logout,doc=doc)
            return True
        except:
            return False




