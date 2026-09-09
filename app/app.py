from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

@app.rout("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__== "__main__":

   app.run('0.0.0.0',port=8080)