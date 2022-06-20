from http import HTTPStatus
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
from email_validator import validate_email, EmailNotValidError

class UserRegisterResource(Resource) :
    def post(self) :

        # {
        #     "username": "홍길동",
        #     "email": "abc@naver.com",
        #     "password": "1234"
        # }

        # 1. 클라이언트가 body 에 보내준 json을 받아온다.
        data = request.get_json()

        # 2. 이메일 주소형식이 제대로 된 주소형식인지
        # 확인하는 코드 작성. 

        try :
            validate_email( data['email'] )
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            return {'error' : str(e)}, 400
        

        #DB에 저장하시말고, 테스트코드만 작성해서 테스트 해보기
            
        return 
