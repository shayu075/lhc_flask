# pip install Flask
from flask import Flask, request, render_template, jsonify
from common.service import get_list_same_num_by_type

app = Flask(__name__)


@app.route('/lhc_flask/ps', methods=['GET'])
def hello_world():
    types = request.args.get('types')

    return jsonify(get_list_same_num_by_type(types))


@app.route('/lhc_flask/', methods=['GET'])
def test_post():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
