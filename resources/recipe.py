from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection

# API 를 만들기 위한 클래스 작성
# class(클래스)란? 변수와 함수로 구성된 묶음
# 클래스는 상속이 가능하다.
# API를 만들기 위한 클래스는, flask_restful 라이브러리의 Resorce 클래스를 상속해서 만들어야 한다.

class RecipeListResource(Resource):
    # restful api의 method에 해당하는 함수 작성
    def post(self):
        # api 실행 코드를 여기에 작성한다.
        pass