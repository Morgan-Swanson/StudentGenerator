#!flask/bin/python
from flask import Flask, jsonify
import student

app = Flask(__name__)

@app.route('/api/<int:number>', methods=['GET'])
def get_students(number):
    return student.get_students(number)

if __name__ == '__main__':
    app.run(debug=True)
