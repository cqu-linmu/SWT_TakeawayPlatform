from flask import Flask

app = Flask(__name__)

#Code app
@app.route('/')
def MainApp():
    return 'Main Launch'

if __name__ == '__main__':
    app.run()