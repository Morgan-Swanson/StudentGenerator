from student import Textgen
from student import Student
from student import Resumegen

print(Textgen.getbio(Student.build_students(1)[0]))
print(Resumegen.student_work(Student.build_students(1)[0]))
print(Resumegen.student_proj(Student.build_students(1)[0]))
print(Resumegen.student_clubs(Student.build_students(1)[0]))