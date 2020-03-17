import os
import random
import pylatex
from student.r1 import Resume1
from student.r2 import Resume2
from student.resume1 import Resume3
from student.resume4 import Resume4
from student.bio import Bio

resumes = [Resume1, Resume2, Resume3, Resume4]

def generateStudentResume(name, email, number, schedule):
    template = random.choice(resumes)
    resume = template(name, email, number)
    resume.finish()
    tex = resume.doc.dumps()

    outfile = name.replace(" ", "") + "_resume"
    outfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../resumes/" + outfile)
    
    resume.doc.generate_tex(outfile)
    resume.doc.generate_pdf(outfile, compiler="/Library/TeX/texbin/pdflatex")




