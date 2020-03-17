from student import Textgen
from student import Student
from student import Resumegen

print(Textgen.getbio(Student.build_students(1)[0]))
print(Resumegen.resumegen(Resumegen.build_students(1)[0]))