import pylatex
from pylatex import Document, Command, UnsafeCommand, Tabular
from pylatex.utils import italic
from pylatex.basic import LineBreak

class Bio:
    def __init__(self):
        borders = {"tmargin": "0in", "rmargin": "0.15in", "lmargin": "0.15in", "bmargin": "0.2in"}
        self.doc = Document(documentclass="bio", geometry_options=borders)
        self.doc.append(Command("begin", "flushleft"))
        self.addCustomCommands()


    def addCustomCommands(self):
        EduEntry = UnsafeCommand('newcommand', r'\EducationEntry', options=1,
                                 extra_arguments=r"""
                            {\bf California Polytechnic State University}
                            \hfill
                            {\em September {#1} - Present}
                        """)

        BoldHeading = UnsafeCommand('newcommand', r'\BoldHeading', options=1,
                                    extra_arguments=r"""
                            {\bf{#1}\sectionskip{\medskip}}
                        """)

        FirstDatedEntry = UnsafeCommand('newcommand', r'\FirstDatedEntry', options=2,
                                        extra_arguments=r"""
                            \text{#1} 
                            \hfill
                            {\em{#2}}
                        """)

        DatedEntry = UnsafeCommand('newcommand', r'\DatedEntry', options=2,
                                   extra_arguments=r"""
                            \item{#1} 
                            \hfill
                            {\em{#2}}
                        """)

        self.doc.append(EduEntry)
        self.doc.append(BoldHeading)
        self.doc.append(DatedEntry)
        self.doc.append(FirstDatedEntry)

    def addTitle(self, student_name, email, number):
        self.doc.preamble.append(Command("name", student_name))
        self.doc.preamble.append(Command("address", f"{number} | {email}"))



    def addProjects(self, projects):
        self.doc.append(Command("begin", ["rSection", "BIOGRAPHY"]))
        for i in range(len(projects)):
            self.doc.append(Command("BoldHeading", projects[i][0]))
            self.doc.append(LineBreak())
            self.doc.append(projects[i][1])

            if i < len(projects) - 1:
                self.doc.append(LineBreak())
                self.doc.append(LineBreak())

        self.doc.append(Command("end", "rSection"))



    def finish(self):
        self.doc.append(Command("end", "flushleft"))


def main():
    resume = Bio()
    resume.addProjects([("Jessica Ferguson",
"My name is Pepe, just kidding my name is Jessica Ferguson."
"I can't stop myself from wasting time on Super Smash Bros Ultimate. "
"You can tell I'm a cool with hobbies like surfing, watching anime, and lifting weights. I try to get stuff done at Greek Week Committee, Mobile App Dev Club, FinTech, and Computer Science and Artificial Intelligence club. College life has let me explore my niche interest. I want to be cool and learn more about Machine Learning ")])
    resume.finish()

    tex = resume.doc.dumps()
    resume.doc.generate_tex("./biotex", compiler="/Library/TeX/texbin/pdflatex")
    resume.doc.generate_pdf("./biopdf", compiler="/Library/TeX/texbin/pdflatex")

if __name__ == '__main__':
    main()