"""
1- itsdangerous的使用
    # 导包
    from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

    # 创建对象Serializer(字符串密钥, 过期时间)
    serializer = Serializer(settings.SECRET_KEY, expires_in=ACCESS_TOKEN_EXPIRES)

    # 字典access_token加密
    token = serializer.dumps(openid)
    # 加密后bytes转字符串
    token = token.decode()
    # 解密
    openid = serializer.loads(token)
"""
