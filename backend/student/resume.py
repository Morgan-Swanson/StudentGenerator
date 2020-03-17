import pdfkit

def save_resume(s):
    pdfkit.from_string(str(s), '/resumes/' + s.name + '.pdf')

def generate_resumes(students):
    for s in students:
        save_resume(s)
