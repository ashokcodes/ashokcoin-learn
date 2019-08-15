from flask_restful import Resource, reqparse, marshal_with
from flask import request
from Interfaces import User

parser = reqparse.RequestParser()


class Auth(Resource):
    def get(self):
        return {'status': False}

    @marshal_with(User.AuthInterface)
    def post(self):
        json_data = request.get_json(force=True)
        username = json_data['username']
        password = json_data['password']
        return {'username': username, 'password': password}
