# pip install Flask
from flask import Flask, request, render_template, jsonify
import common.service as os

app = Flask(__name__)


@app.route('/ps', methods=['POST'])
def hello_world():
    types = request.form['types']
    return jsonify(os.get_list_same_num_by_type(types))


@app.route('/', methods=['GET'])
def test_post():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
