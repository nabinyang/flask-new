from flask import jsonify, Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():

@app.route('/echo_call/<param>') #get echo api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/echo_call', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)
