from flask import jsonify, Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    params = request.get_json()
    return render_template('./index.html', params = params)
