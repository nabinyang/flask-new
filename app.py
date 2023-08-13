from flask import jsonify, Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')

@app.route('/get', methods=['GET'])
def get():
    return jsonify({"data": data, "status": HTTPStatus.OK})

@app.route('/post', methods=['POST'])
def post():
    params = request.get_json()
    print(params)

    return jsonify({"data": params, "status": HTTPStatus.OK})
