import datetime
import allure
import pytest
#1、定义装饰2层函数
from Common.dir_config import screenshot_dir
from conftest import access_web1


def screenshot_allure(func):
    def get_err_screenshot(self,*args,**kwargs,):
#2、定义内部函数，拍图操作
        try:
            func(self,*args,**kwargs)
        except Exception as e:
            png = access_web1[0].get_screenshot_as_png()
            name = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            allure.attach(png, name, allure.attachment_type.PNG)
            # png_dir = screenshot_dir
            # allure.attach.file(png_dir, allure.attachment_type.PNG)
            raise e
#3、返回内部函数名称
    return get_err_screenshot