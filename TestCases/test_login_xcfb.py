import pytest

from PageObjects.index_page_xcfb import IndexPageXcfb
from TestDatas import login_datas_xcfb as LD


@pytest.mark.usefixtures("access_web1")
@pytest.mark.usefixtures("refresh_page1")
class TestLoginXcfb():


    #异常用例 - 登录失败-数据不正确
    @pytest.mark.parametrize("data",LD.err_data)
    def test_login_0_user_wrongFormat(self,data,access_web1):
        """
        异常用例 - 登录失败-数据不正确
        步骤:
         1.输入用户名：XX 密码：XX 点击登录
         2. 断言： 登录页面 提示 - XXX
              登录页面中 - 获取提示框的文本内容
              比对文本内容 与 期望的值 是否相等。
        :param data:
        :param access_web1:
        :return:
        """
        access_web1[1].login(data["username"], data["passwd"])
        assert access_web1[1].get_errorMsg_from_pageCenter() == data["check"]
        ####***不要忘记()***,...get_errorMsg_from_pageCenter(),经常容易忘记

    # 异常用例 - 忘记密码-数据不正确
    @pytest.mark.parametrize("data", LD.code_data)
    def test_login_forget_passwd(self,data,access_web1):
        """
        步骤：
        1.点击忘记密码
        2.输入电话号码、输入短信验证码
        3.点击获取验证码/下一步
        4.断言 -- 输入框下
        :param data:
        :param access_web1:
        :return:
        """
        access_web1[1].forget_passwd(data["phone"],data["code"],data["type"])
        if data["asert"] == "txt":
            assert access_web1[1].get_error_msg() == data["check"]
        else:
            assert access_web1[1].get_code_msg() == data["check"]



    # 正常用例 - 登录成功  (#fixture的函数名称，用来接收它的返回值)
    @pytest.mark.xcfb
    def test_login_1_success(self, access_web1):
        """
        正常用例 - 登录成功
        步骤 :
        1.输入用户名：XX 密码：XX 点击登录
        2.断言 ：首页当中 - 能否找到 用户名 这个元素
        :param access_web1:
        :return:
        """
        access_web1[1].login(LD.success_data["username"], LD.success_data["passwd"])
        assert IndexPageXcfb(access_web1[0]).isExist_logout_ele()






# if __name__ == '__main__':
#     pytest.main()


