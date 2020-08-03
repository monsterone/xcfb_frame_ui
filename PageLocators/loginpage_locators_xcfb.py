

from selenium.webdriver.common.by import By

# 登录页面元素定位
class LoginPageLocatorXcfb:
    """
    xcfb登录页面元素定位
    """

    # 用户名输入框
    name_text = (By.XPATH, '//*[@class="el-input__inner" and @placeholder="请输入账号名"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//*[@class="el-input__inner" and @placeholder="请输入密码"]')
    # 登录按钮
    login_but = (By.XPATH, '//div[@class="login-btn"]/button')


    # 错误提示框 - 登录页面正中间
    errorMsg_from_pageCenter = (By.XPATH, '//p[@class="el-message__content"]')


    ## 忘记密码
    but_forget = (By.CSS_SELECTOR,'.forget-password')
    # 手机账号输入框
    phone_input = (By.XPATH, '//label[@for="phoneNumber"]/following-sibling::div/div/input')
    # 验证码输入框
    code_input = (By.XPATH, '//label[@for="code"]/following-sibling::div/div/input')
    # 获取验证码按钮
    code_but = (By.CSS_SELECTOR,'.verification-code')
    # 下一步按钮
    next_but = (By.XPATH,' //span[text()="下一步"]')

    # 请输入正确手机号、请输入验证码文本提示：
    errorMsg_txt = (By.CSS_SELECTOR,'.el-form-item__error')
    # 短信验证码错误   弹窗提示
    codeError_alert = (By.CSS_SELECTOR,'.el-message__content')