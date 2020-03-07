# StudentGenerator
## Goals
* Generate a statistically accurate computer science student
* Produce a natural language biography of the student
* Simulates their educational development and skills
* Generate a complete resume of the student

## How to Generate Students
Javascript code to run student generator
```
const spawn = require("child_process").spawn;
const pythonProcess = spawn('python',["student.py", number_of_students]);
```
How to read json file in javascript
```
import students from "./students.json";
```
