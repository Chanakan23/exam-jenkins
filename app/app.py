from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/is_leap_year/<int:year>')
def is_leap_year(year):
    if year % 4 == 0:
        return 'True'
    else:
        return 'False'

if __name__ == '__main__':
    app.run()