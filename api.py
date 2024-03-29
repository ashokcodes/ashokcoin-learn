from flask import Flask
from flask_restful import Resource, Api, reqparse
from controllers import User

app = Flask(__name__)
api = Api(app)


api.add_resource(User.Auth, '/auth')

if __name__ == '__main__':
    app.run(debug=True)
