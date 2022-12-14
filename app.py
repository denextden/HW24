import os
from utils import build_query
from flask import Flask, request, Response
from flask_restx import abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST', 'GET'])
def perform_query() -> Response:
    cmd_1 = request.args.get('cmd_1')
    value_1 = request.args.get('value_1')
    cmd_2 = request.args.get('cmd_2')
    value_2 = request.args.get('value_2')
    file_name = request.args.get('file_name')

    if not (cmd_1 and value_1 and file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, str(file_name))
    if not os.path.exists(file_path):
        return abort(400, 'Wrong filepath')

    with open(file_path) as file:
        res = build_query(str(cmd_1), str(value_1), file)
        if cmd_2 and value_2:
            res = build_query(str(cmd_2), str(value_2), iter(res))

    return app.response_class("\n".join(res), content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
