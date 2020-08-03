from Common.random_data import get_random

test_data = get_random()

# 正常场景 - 登录成功-测试数据
success_data = {"username":"more","passwd":"666666","check":"登录成功","explain":"正确用户名密码"}
# success_data = {"username":"monster","passwd":"111111","check":"登录成功","explain":"正确用户名密码"}

# 异常用例 - 登录失败-测试数据
err_data = [
    {"username":"","passwd":"","check":"请输入账号名","explain":"什么都不输"},
    {"username":"", "passwd": "111111", "check": "请输入账号名","explain":"只输入密码"},
    {"username":"haha", "passwd":"", "check": "请输入密码","explain":"只输入账号"},
    {"username":test_data, "passwd":test_data, "check": "账号或密码错误，还有[4]次将锁定账号","explain":"账号密码错误"},
    {"username":test_data, "passwd":test_data, "check": "账号或密码错误，还有[3]次将锁定账号","explain":"账号密码错误"},
    {"username":test_data, "passwd":test_data, "check": "账号或密码错误，还有[2]次将锁定账号","explain":"账号密码错误"},
    {"username":test_data, "passwd":test_data, "check": "账号或密码错误，还有[1]次将锁定账号","explain":"账号密码错误"},
    {"username":test_data, "passwd":test_data, "check": "账号或密码错误，账号已锁定","explain":"账号密码错误"},
    {"username":test_data, "passwd":test_data, "check": "请29分钟后再试或使用忘记密码找回密码","explain":"账号密码错误"}
]

# 异常用例 - 忘记密码-测试数据
code_data = [
    {"phone":"", "code":"", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"132142", "code":"", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"132142464574577", "code":"", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"ewrfefif", "code":"", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"", "code":"4356", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"132142", "code":"4356", "check": "请输入正确的手机号码","type":"y","asert":"txt"},
    {"phone":"", "code":"", "check": "请输入正确的手机号码","type":"n","asert":"txt"},
    {"phone":"", "code":"4356", "check": "请输入正确的手机号码","type":"n","asert":"txt"},
    {"phone":"18166666666", "code":"", "check": "请输入验证码","type":"n","asert":"txt"},
    {"phone":"18166666666", "code":"4356", "check": "短信验证码错误","type":"n","asert":"alert"}
]


