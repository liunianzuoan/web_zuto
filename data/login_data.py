


# 分组的依据：操作步骤，表现形式是否一样
# 正确的用户信息
user_correct = {"phone":"18684720553 ","password":"python"}

# 错误的用户信息   //div[@class='form-error-info']

user_incorrect = [{"phone":"","password":"","expected":"请输入手机号"},
                  {"phone":"12","password":"","expected":"请输入正确的手机号"},
                  {"phone":"18684720553","password":"","expected":"请输入密码"}
                  ]

# 弹框形式的用户信息   # //div[@class='layui-layer-content']
user_unauthorized = [{"phone":"13825802580", "password":"123","expected":"此账号没有经过授权，请联系管理员!"},
                     {"phone":"18684720553","password":"111","expected":"帐号或密码错误!"}]