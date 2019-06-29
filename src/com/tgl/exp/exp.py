# -*- coding: UTF-8 -*-
#from src.com.tgl.exp.app.user_service import create_user

import src.com.tgl.exp.app.user_service as service
from src.com.tgl.exp.domain.user_entity import UserEntity

from flask import Flask,request
import json



app = Flask(__name__)

def main():
    app.run()


@app.route('/createUser',methods=['post'])
def create_user():
    print("request.data: %s" % request.data)

    req_val = request.data.decode('utf-8')

    req_json = json.loads(req_val)

    #user = service.create_user('liuwei',33)
    user = UserEntity(**req_json)

    # 序列化json
    result = json.dumps(user.__dict__)

    # 反序列化
    usercp = UserEntity(**json.loads(result))



    return usercp.get_name()





if __name__ == '__main__':
    main()
