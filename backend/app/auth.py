from flask_jwt_extended import JWTManager

jwt = JWTManager()

# 初始化 JWT
def init_jwt(app):
    jwt.init_app(app) 