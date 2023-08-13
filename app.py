from flask import jsonify, Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')

@app.route('/post', methods=['POST'])
def post():
    params = request.get_json()
    print(params['id'])
    print(params['nickname'])
    print(params['email'])
    print(params['gender'])
    print(params['nickname'])
    print(params['ageRange'])
    
    return jsonify({"data": params})
