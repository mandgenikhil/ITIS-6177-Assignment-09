from flask import Flask,request

app = Flask(__name__)

@app.route("/say")
def hello_world():
    keyword = request.args.get('keyword')
    if keyword:
        return "Nikhil Mandge says "+keyword 
    else:
        return "Please add correct url"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)