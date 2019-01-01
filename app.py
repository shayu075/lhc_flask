# pip install Flask
from flask import Flask, request, render_template, jsonify
from common.service import get_list_same_num_by_type

app = Flask(__name__)


@app.route('/ps', methods=['POST'])
def hello_world():
    types = request.form['types']

    return jsonify(get_list_same_num_by_type(types))


@app.route('/', methods=['GET'])
def test_post():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
