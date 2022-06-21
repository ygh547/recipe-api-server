from distutils.command.config import config
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResoure
from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist


app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(config)
# JWT 토큰 라이브러리 만들기
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

# 로그아웃 된 토큰이 들어있는 set을, jwt에 알려준다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 resource(API 코드)를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResoure, '/recipes/<int:recipe_id>/publish')
api.add_resource(UserRegisterResource, '/users/register')
api.add_resource(UserLoginResource, '/users/login')
api.add_resource(UserLogoutResource, '/users/logout')








if __name__ == '__main__' :
    app.run()