import os
import random
import pylatex
from student.r1 import Resume1
from student.r2 import Resume2
from student.resume1 import Resume3
from student.resume4 import Resume4
from student.bio import Bio
from student import Resumegen

resumes = [Resume1, Resume2, Resume3, Resume4]
years = {"first" : ("2019", "2023"), 
            "second" : ("2018", "2022"),
            "third" : ("2017", "2021"),
            "fourth" : ("2016", "2020")}

def generateStudentResume(student, schedule):
    template = random.choice(resumes)
    resume = template(student.name, student.email, student.phone)
    school_years = years[student.school_year.lower()]
    major = Resumegen.student_major()

    experiences = [Resumegen.student_work(student), Resumegen.student_work(student), Resumegen.student_work(student)]
    projects = [Resumegen.student_proj(student), Resumegen.student_proj(student), Resumegen.student_proj(student)]

    resume.addEducation(school_years[0], school_years[1], major)
    resume.addExperience(experiences)
    resume.addProjects(projects)
    resume.addRelevantCoursework(schedule)
    resume.addSkills("Soft", student.soft_skills)

    resume.finish()
    tex = resume.doc.dumps()

    print(student.key)
    outfile = student.key + "_resume"
    outfile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/react/resumes/" + outfile))
    
    resume.doc.generate_tex(outfile)
    resume.doc.generate_pdf(outfile, compiler="/Library/TeX/texbin/pdflatex")

def generateStudentBio(name, key, biotext):
    template = Bio()
    template.addProjects([(name, biotext)])
    template.finish()
    tex = template.doc.dumps()

    outfile = key + "_bio"
    outfile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/react/bios/" + outfile))

    template.doc.generate_tex(outfile)
    template.doc.generate_pdf(outfile, compiler="/Library/TeX/texbin/pdflatex")

