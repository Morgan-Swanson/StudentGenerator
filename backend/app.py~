#!flask/bin/python
from flask import Flask, jsonify
from flask import render_template
from student import Student
app = Flask(__name__)


@app.route('/api/<int:number>')
def get(number):
    return jsonify(Student.get_students(number))

#return jsonify(Student.get_students(number))

@app.route('/')
def hello_world():
    return render_template('index.html',
                           flask_token="Hello world!")


if __name__ == '__main__':
    app.run(debug=True)
