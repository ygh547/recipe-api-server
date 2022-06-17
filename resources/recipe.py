from http import HTTPStatus
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector

# API 를 만들기 위한 클래스 작성
# class(클래스)란? 변수와 함수로 구성된 묶음
# 클래스는 상속이 가능하다.
# API를 만들기 위한 클래스는, flask_restful 라이브러리의 Resorce 클래스를 상속해서 만들어야 한다.

# name = '순두부'
# description = '순두부찌개 만드는법'
# cook_time = 45
# directions = '물넣고 두부넣고 조개넣고 끓인다'

class RecipeListResource(Resource):
    # restful api의 method에 해당하는 함수 작성
    def post(self):
        # 클라이언트에서, bodt 부분에 작성한 json을 받아오는 코드
        data = request.get_json()
        
        # 받아온 데이터를 db에 저장하면 된다.
        try :
            # 데이터 insert
            #1. DB에 연결
            connection = get_connection()
            #2. 쿼리문 만들기
            query = '''insert into recipe
                    (name, description, cook_time, directions)
                    values
                    ( %s , %s, %s, %s);'''

            record = (data['name'], data['description'], data['cook_time'], data['directions'])

            #3. 커서를 가져온다.
            cursor = connection.cursor()
            #4. 쿼리문을 커서를 이용해서 실행한다.
            cursor.execute(query, record)
            #5. 커넥션을 커밋해줘야 한다. => 디비에 영구적으로 반영하라는 뜻
            connection.commit()
            #6. 자원 해제
            cursor.close()
            connection.close()

        # 정상적이지 않을때
        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503

        return {"result" : "success"}, 200