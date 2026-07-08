from flask import Flask

app = Flask(__name__)

@app.route('/')
def Test_system():
    return '<h1>Welcome to the Test System</h1> <p>I want to learn about python programming and use docker tp deply it.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    

