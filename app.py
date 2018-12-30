# pip install Flask
from flask import Flask, request, render_template, jsonify
# pip install Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import common.service as os

app = Flask(__name__)
# pip3 install flask-mysqldb
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/my_study?charset=utf8'
db = SQLAlchemy(app)


@app.route('/ps', methods=['POST'])
def hello_world():
    types = request.form['types']
    return jsonify(os.get_list_same_num_by_type(types))


@app.route('/', methods=['GET'])
def test_post():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
