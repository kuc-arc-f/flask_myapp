
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='localhost',  debug=True)
    #app.run(host='localhost', port=80, debug=True)
    #app.run()
