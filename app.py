from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello this my new website!</h1><p>Continuous Integration and Continuous Deployment is working.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

