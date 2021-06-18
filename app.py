from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Float, Integer
import os

app = Flask(__name__)
# db configaration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mine.db')
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return jsonify(message="Hello, World!")\



@app.route("/parameters")
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age > 18:
        return jsonify(message="OK"+name+' yo', data=['age:89', 'name:koi'], erros=''), 200
    else:
        return jsonify(message="NOT var OK"+name+' not yo', erros='not possible'), 404


@app.route("/variables/<string:name>/<int:age>")
def variables(name: str, age: int):
    if age < 18:
        return jsonify(message=" Not OK "+name, error='your age is '+str(age)), 401
    else:
        return jsonify(message="OK "+name), 200


# models
class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)


class Family(db.Model):
    __tablename__ = 'family'
    familyId = Column(Integer, primary_key=True)
    relation = Column(String)
    age = Column(Integer)
    distanceLocation = Column(Float)



if __name__ == '__main__':
    app.run(debug=True)
