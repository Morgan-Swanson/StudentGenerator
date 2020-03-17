import pylatex
from pylatex import Document, Command, UnsafeCommand, Tabular
from pylatex.utils import italic, NoEscape
from pylatex.basic import LineBreak

class Resume2:
    def __init__(self, name, email, number):
        borders = {"tmargin": "1.25in", "rmargin": "1in", "lmargin": "1in", "bmargin": "1.25in"}
        self.doc = Document(documentclass="article", document_options=["letterpaper", "11pt", "oneside"], 
                        geometry_options=borders, page_numbers=False)
        self.doc.preamble.append(Command("usepackage", "graphicx"))
        self.doc.append(Command("begin", "flushleft"))
        self.addCustomCommands()
        self.addTitle(name, email, number)
        self.doc.append(Command("begin", ["tabular", NoEscape(r"@{} l l")]))

    def addCustomCommands(self):
        NameEntry = UnsafeCommand('newcommand', r'\NameEntry', options=1, 
                                extra_arguments=r"""
                            \noindent \LARGE{\textbf{#1}}
                            \linebreak
                            \vspace{-2ex}
                            \hrule
                            \normalsize
                        """)

        PageSpacing = UnsafeCommand('newcommand', r'\PageSpacing', options=0,
                                extra_arguments=r"""
                            \vspace{1em}
                            \noindent
                        """)
        
        EducationEntry = UnsafeCommand('newcommand', r'\EducationEntry', options=3,
                                extra_arguments=r"""
                            \Large{Education}
                            & \textbf{California Polytechnic State University, San Luis Obispo}
                            & \linebreak
                            & B.S. {#1}
                            & \linebreak
                            & September {#2} - June {#3} \\
                            \\
                        """)

        WorkEntry = UnsafeCommand('newcommand', r'\WorkEntry', options=1,
                                extra_arguments=r"""
                            & \parbox{5.0in}{#1} \\
                            \\
                        """)

        WorkEntryTitle = UnsafeCommand('newcommand', r'\WorkEntryTitle', options=1,
                                extra_arguments=r"""
                            & \textbf{#1}
                            \\
                        """)

        ItemEntry = UnsafeCommand('newcommand', r'\ItemEntry', options=1,
                                extra_arguments=r"""
                            & {#1} \\
                        """)

        EndSection = UnsafeCommand('newcommand', r'\EndSection', options=0,
                                extra_arguments=r"""
                            & \\
                        """)

        self.doc.append(NameEntry)
        self.doc.append(PageSpacing)
        self.doc.append(EducationEntry)
        self.doc.append(WorkEntryTitle)
        self.doc.append(WorkEntry)
        self.doc.append(ItemEntry)
        self.doc.append(EndSection)

    def addTitle(self, student_name, email, number):
        self.doc.append(Command("NameEntry", student_name))
        self.doc.append(Command("begin", "flushright"))
        self.doc.append(email + ", " + number)
        self.doc.append(Command("end ", "flushright"))
        self.doc.append(Command("PageSpacing"))

    def addEducation(self, year, grad, major):
        self.doc.append(Command("EducationEntry", [major, year, grad]))

    """ Projects must be given as a list of tuples in the format (name, date, position, description) """
    def addExperience(self, jobs):
        self.doc.append(Command("Large", "Work Experience"))
        for job in jobs:
            self.doc.append(Command("WorkEntryTitle", job[0]))
            self.doc.append(Command("WorkEntry", job[2] + " - " + job[1]))
            self.doc.append(Command("WorkEntry", job[3]))

    def addProjects(self, projects):
        self.doc.append(Command("Large", "Projects"))
        for project in projects: 
            self.doc.append(Command("WorkEntryTitle", project[0]))
            self.doc.append(Command("WorkEntry", project[1]))

    def addRelevantCoursework(self, classes):
        self.doc.append(Command("Large", "Courses"))
        for c in classes:
            self.doc.append(Command("ItemEntry", c))
        self.doc.append(Command("EndSection"))

    def addExtracurriculars(self, activities):
        self.doc.append(Command("Large", "Activities"))
        for act in  activities:
            self.doc.append(Command("ItemEntry", act[0]))
        self.doc.append(Command("EndSection"))

    """ Type should be either 'Techincal' or 'Soft' """
    def addSkills(self, type, skills):
        self.doc.append(Command("Large", type + " Skills"))
        self.doc.append(Command("ItemEntry", ", ".join(skills)))
        self.doc.append(Command("EndSection"))

    def finish(self):
        self.doc.append(Command("end", "tabular"))
        self.doc.append(Command("end", "flushleft"))

def main():
    resume = Resume2("Ariel Chen", "achen@calpoly.edu", "925-786-3014")
    resume.addEducation("2017", "2021", "Computer Science")
    resume.addExperience([("SJ Contracts, Pune", "June 2016", "Site Engineer", "On-site internship under this leading construction company. Learned and implemented various aspects such as quantity estimation, labour management and safety precautions.")])
    resume.addProjects([("Dynamic Analysis of Buckling Restrained Braces", "The project aims at designing and fabrication of two Buckling Restrained Braces which were analyzed under dynamic loading. As alternative for conventional braces, these BRBs are also beneficial for seismic retro-fitting in RCC and steel structures."), 
                        ("Indirect Model Analysis of Structures", "Presented a Seminar on Indirect Model Analysis, explaining the method to compute response of Prototype from the Influence lines obtained from Model. Use of Muller Breslau Principle in Indirect Model Analysis and the Similitude between prototype and  model."), 
                        ("Microtunneling", "Presented a seminar on Micro Tunneling, explaining its advantages over conventional method of drainage laying systems. Analysis considering direct and indirect cost of micro tunneling was also discussed.")])
    resume.addRelevantCoursework(["CSC 482 - NLP", "CSC 430 - Programming Languages", "CSC 480 - Artificial Intelligence",  
                                        "CSC 421 - Security"])
    resume.addExtracurriculars([("Women in Software and Hardware", "October 2017 - Present"), 
                                ("Society of Women Engineers", "January 2018 - Present")])
    resume.addSkills("Soft", ["Leadership", "Teamwork", "Learns quickly"])
    resume.addSkills("Technical", ["Python", "Javascript"])
    resume.finish()

    tex = resume.doc.dumps()
    resume.doc.generate_tex("./resume_2")
    resume.doc.generate_pdf("testpdf2", compiler="/Library/TeX/texbin/pdflatex")
   

if __name__ == '__main__':
    main()