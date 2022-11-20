"""
1- 用户点击QQ登录->服务器拼接QQ扫码页面地址响应(拼接开发者id,密码,回调地址等)

2- 用户扫码授权->QQ互联拼接code返回给服务器

3- 服务器通过code获取access_token

4- 服务器通过access_token获取唯一标识用户QQ号码的openid

5- 进行后续逻辑

"""
