#!flask/bin/python
from flask import Flask, jsonify
from flask import render_template
from student import Student
app = Flask(__name__)

def convert_gender(num):
    if num == 0:
        return None
    elif num == 1:
        return "Male"
    else:
        return "Female"

def convert_year(num):
    if num == 0:
        return None
    elif num == 1:
        return "First"
    elif num == 2:
        return "Second"
    elif num == 3:
        return "Third"
    else:
        return "Fourth"
       
@app.route('/api/<int:number>-<int:gender>-<int:year>')
def get(number, gender, year):
    return jsonify(Student.get_students(number, 
                                        convert_gender(gender),
                                        convert_year(year)))

@app.route('/')
def hello_world():
    return render_template('index.html',
                           flask_token="Hello world!")


if __name__ == '__main__':
    app.run(debug=True)
