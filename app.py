from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResoure
from resources.user import UserRegisterResource


app = Flask(__name__)

api = Api(app)

# 경로와 resource(API 코드)를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResoure, '/recipes/<int:recipe_id>/publish')
api.add_resource(UserRegisterResource, '/users/register')








if __name__ == '__main__' :
    app.run()