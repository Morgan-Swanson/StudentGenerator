import pylatex
from pylatex import Document, Command, UnsafeCommand, Tabular
from pylatex.utils import italic
from pylatex.basic import LineBreak


class Resume4:
    def __init__(self, name, email, number):
        borders = {"tmargin": "0.6in", "rmargin": "0.75in", "lmargin": "0.75in", "bmargin": "0.6in"}
        self.doc = Document(documentclass="resume4", geometry_options=borders)
        self.doc.append(Command("begin", "flushleft"))
        self.addCustomCommands()
        self.addTitle(name, email, number)

    def addCustomCommands(self):
        EduEntry = UnsafeCommand('newcommand', r'\EducationEntry', options=1,
                                 extra_arguments=r"""
                            \fbox{\bf California Polytechnic State University}
                            \hfill
                             \fbox{\em September {#1} - Present}
                        """)

        BoldHeading = UnsafeCommand('newcommand', r'\BoldHeading', options=1,
                                    extra_arguments=r"""
                             \fbox{\bf{#1}}
                        """)

        FirstDatedEntry = UnsafeCommand('newcommand', r'\FirstDatedEntry', options=2,
                                        extra_arguments=r"""
                            \text\fbox{#1} 
                            \hfill
                            \fbox{\em{#2}}
                        """)

        DatedEntry = UnsafeCommand('newcommand', r'\DatedEntry', options=2,
                                   extra_arguments=r"""
                            \item\fbox{#1} 
                            \hfill
                            \fbox{\em{#2}}
                        """)

        self.doc.append(EduEntry)
        self.doc.append(BoldHeading)
        self.doc.append(DatedEntry)
        self.doc.append(FirstDatedEntry)

    def addTitle(self, student_name, email, number):
        self.doc.preamble.append(Command("name", student_name))
        self.doc.preamble.append(Command("address", f"{number} / {email}"))

    def addEducation(self, year, grad, major):
        self.doc.append(Command("begin", ["rSection", "Education"]))
        self.doc.append(Command("EducationEntry", year))
        self.doc.append(LineBreak())
        self.doc.append("Bachelor of Science in " + major)
        self.doc.append(LineBreak())
        self.doc.append("Estimated graduation date: June " + grad)
        self.doc.append(Command("end", "rSection"))

    """ Projects must be given as a list of tuples in the format (name, description) """

    def addProjects(self, projects):
        self.doc.append(Command("begin", ["rSection", "Projects"]))
        for i in range(len(projects)):
            self.doc.append(Command("BoldHeading", projects[i][0]))
            self.doc.append(LineBreak())
            self.doc.append(projects[i][1])

            if i < len(projects) - 1:
                self.doc.append(LineBreak())
                self.doc.append(LineBreak())

        self.doc.append(Command("end", "rSection"))

    """ Projects must be given as a list of tuples in the format (name, date, position, description) """

    def addExperience(self, jobs):
        self.doc.append(Command("begin", ["rSection", "Related Work Experience"]))
        for job in jobs:
            self.doc.append(Command("begin", ["rSubsection", job[0], italic(job[1]), job[2], '']))
            self.doc.append(Command("item", job[3]))

        self.doc.append(Command("end", "rSubsection"))
        self.doc.append(Command("end", "rSection"))

    """ Type should be either 'Techincal' or 'Soft' """

    def addSkills(self, type, skills):
        self.doc.append(Command("begin", ["rSection", type + " Skills"]))
        self.doc.append(" / ".join(skills))
        self.doc.append(Command("end", "rSection"))

    """ Extracurriculars must be given as a list of tuples in the format (name, date) """

    def addExtracurriculars(self, activities):
        self.doc.append(Command("begin", ["rSection", "Extracurriculars"]))
        self.doc.append(Command("FirstDatedEntry ", activities[0]))
        for act in activities[1:]:
            self.doc.append(Command("DatedEntry ", act))

        self.doc.append(Command("end", "rSection"))

    def addRelevantCoursework(self, classes):
        self.doc.append(Command("begin", ["rSection", "Coursework"]))
        self.doc.append(Command("text->", classes[0]))
        for c in classes[1:]:
            self.doc.append(Command("item->", c))
        self.doc.append(Command("end", "rSection"))

    def finish(self):
        self.doc.append(Command("end", "flushleft"))


def main():
    resume = Resume4("Ariel Chen", "achen@calpoly.edu", "925-786-3014")
    resume.addEducation("2017", "2021", "Computer Science")
    resume.addProjects([("Dynamic Analysis of Buckling Restrained Braces",
                         "The project aims at designing and fabrication of two Buckling Restrained Braces which were analyzed under dynamic loading. As alternative for conventional braces, these BRBs are also beneficial for seismic retro-fitting in RCC and steel structures."),
                        ("Indirect Model Analysis of Structures",
                         "Presented a Seminar on Indirect Model Analysis, explaining the method to compute response of Prototype from the Influence lines obtained from Model. Use of Muller Breslau Principle in Indirect Model Analysis and the Similitude between prototype and  model."),
                        ("Microtunneling",
                         "Presented a seminar on Micro Tunneling, explaining its advantages over conventional method of drainage laying systems. Analysis considering direct and indirect cost of micro tunneling was also discussed.")])
    resume.addExperience([("SJ Contracts, Pune", "June 2016", "Site Engineer",
                           "On-site internship under this leading construction company. Learned and implemented various aspects such as quantity estimation, labour management and safety precautions.")])
    resume.addExtracurriculars([("Women in Software and Hardware", "October 2017 - Present"),
                                ("Society of Women Engineers", "January 2018 - Present")])
    resume.addRelevantCoursework(
        [("CSC 482 - NLP", "CSC 430 - Programming Languages"), ("CSC 480 - Artificial Intelligence",
                                                                "CSC 421 - Security"),
         ("CSC 466 - KDD", "CSC 481 - Human Computer Interaction")])
    resume.addSkills("Soft", ["Leadership", "Teamwork", "Learns quickly"])
    resume.addSkills("Technical", ["Python", "Javascript"])
    resume.finish()

    tex = resume.doc.dumps()
    resume.doc.generate_tex("./resume4")
    resume.doc.generate_pdf("testpdf4", compiler="/Library/TeX/texbin/pdflatex")



if __name__ == '__main__':
    main()