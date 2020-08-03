
import os,sys

from PageLocators.loginpage_locators_xcfb import LoginPageLocatorXcfb as loc
#引入页面元素定位页面，页可以继承该类，但元素多了不好区分，长远考虑用loc快速找到定位元素
from Common.basepage import BasePage
class LoginPageXcfb(BasePage):
    """
    xcfb登录页面PageOboect
    """

    #登录操作
    def login(self,username,passwd):
        """
        登录操作
        步骤：
        1.输入用户名
        2.输入密码
        3.点击登录
        :param username:
        :param passwd:
        :return:
        """
        doc = "登录页面_登录功能"

        if username == '' and passwd == '':
            self.wait_eleVisible(loc.login_but, doc=doc)
            self.click_element(loc.login_but, doc)
        elif username == '':
            self.wait_eleVisible(loc.pwd_text, doc=doc)
            self.input_text(loc.pwd_text, passwd, doc)
            self.click_element(loc.login_but, doc)
        elif passwd == '':
            self.wait_eleVisible(loc.name_text, doc=doc)
            self.input_text(loc.name_text, username, doc)
            self.click_element(loc.login_but, doc)
        else:
            self.wait_eleVisible(loc.name_text,doc=doc)
            self.input_text(loc.name_text,username,doc)
            self.input_text(loc.pwd_text,passwd,doc)
            self.click_element(loc.login_but,doc)

        #两种方式都可以
        # self.wait_eleVisible(loc.name_text, doc=doc)
        # self.input_text(loc.name_text, username, doc)
        # self.input_text(loc.pwd_text, passwd, doc)
        # self.click_element(loc.login_but, doc)



    # 获取登录错误提示信息-登录页面正中间 断言
    def get_errorMsg_from_pageCenter(self):
        """
        断言：获取登录错误提示信息 - 登录页面正中间
        :return:
        """
        doc = "登录页面_获取错误提示信息"
        self.wait_eleVisible(loc.errorMsg_from_pageCenter, doc=doc)
        return self.get_text(loc.errorMsg_from_pageCenter, doc)



    # 忘记密码
    def forget_passwd(self,phone,code,type):
        """
        忘记密码
        步骤：
        1.点击忘记密码
        2.输入电话号码
        3.输入短信验证码
        4.点击获取验证码/下一步
        :param phone:
        :param code:
        :return:
                """
        doc = "登录页面_忘记密码"

        self.wait_eleVisible(loc.but_forget, doc=doc)
        self.click_element(loc.but_forget,doc)
        self.wait_eleVisible(loc.phone_input,doc=doc)
        # self.input_text(loc.phone_input,phone,doc)
        # self.input_text(loc.code_but,code,doc)
        self.ActionChains_text(loc.phone_input,phone,doc)
        self.ActionChains_text(loc.code_input,code,doc)
        if type == 'y':
            self.click_element(loc.code_but,doc)
        else:
            self.click_element(loc.next_but,doc)


    # 获取手机号、验证码提示信息 断言
    def get_error_msg(self):
        """
        断言:获取手机号、验证码提示信息
        :return:
        """
        doc = "登录页面_忘记密码_错误提示"
        self.wait_eleVisible(loc.errorMsg_txt, doc=doc)
        return self.get_text(loc.errorMsg_txt, doc)

    # 获取错误验证码弹框提示 断言
    def get_code_msg(self):
        """
        断言:获取错误验证码弹框提示
        :return:
        """
        doc = "登录页面_忘记密码_错误提示"
        self.wait_eleVisible(loc.codeError_alert,doc=doc)
        return self.get_text(loc.codeError_alert, doc)











