# pip install Flask
from flask import Flask, request, render_template, jsonify
from common.service import get_list_same_num_by_type

app = Flask(__name__)


# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
#     # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response


@app.route('/lhc_flask/ps', methods=['GET'])
def hello_world():
    types = request.args.get('types')
    year = request.args.get('year')
    month = request.args.get('month')

    return jsonify(get_list_same_num_by_type(types, year, month))


@app.route('/lhc_flask/', methods=['GET'])
def test_post():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
