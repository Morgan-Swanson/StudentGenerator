#!flask/bin/python
from flask import Flask, jsonify
from flask import render_template
from student import Student
app = Flask(__name__)


@app.route('/api/<int:number>-<int:gender>-<int:year>')
def get(number, gender, year):
    print(gender, year)
    return jsonify(Student.get_students(number))

@app.route('/')
def hello_world():
    return render_template('index.html',
                           flask_token="Hello world!")


if __name__ == '__main__':
    app.run(debug=True)
