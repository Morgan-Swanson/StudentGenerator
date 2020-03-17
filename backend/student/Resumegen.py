import random

major_list = ["Software Engineering","Computer Science"]


projects_front_4 = [("Movie Search App","Building this application I learned "
            "React Skills using the relatively new "
            "Hooks API. The example projects makes use of React components and CSS styling."),
            ("Chat App","The project shows how to setup a Vue app from scratch, creating components, handling state, creating route, connecting to a third party service and even handling authentication.")
            ,("Weather App","Project implements Firebase, CSS with Grid Layout and Flexbox to create a ploshied product."),
                    ("Re-create Giphy","a web app which uses a search input and Giphy’s API to display giphs on a page. Used JavaScript and jQuery.")]
projects_low_4 = [("Custom Operating System","Built an operating system from scratch. Learned about Linux as a development environment and x86 assembly in-depth.")]
projects_back_4 = [("FTP Client","Built a FTP client that supports secure file transfer"),("Sports Page","Uses a  automatically updating data set. Learned about web scraping and web input to CSV output")]
projects_graphics_4 = [("Procedurally Generated Map Maker","Browser-based application that allows users to procedurally generate a terrain map based on a random seed."),("Pixel art generator","Built a tool that takes an image as input and samples the image to produce pixel art as output. Learned about CSS and Pylatex. ")]
projects_Machine_4 = [("Niche Chatbot","Used NLP to create a chatbot that can talk about any topic it can scrape from wikipeda "),("Spam Classifier","Uses content of email to detect Spam or Non Spam emails. Learned about NLP and Neural Nets.")]
projects_Security_4 = [("Privileged access management","Covers human and non-human system accounts and supports a combination of on-premises, cloud, and hybrid environments, as well as APIs for automation.")
    ,("Reputation Server","Able to track a users behavior based on feed back. Learned about SQL"),("Firewall","Created a secure and dynamic firewall using C++ learned a lot about algorithms")]


#work experience
companies_name = ["Amazon","Google","Apple","Microsoft","Workday","Salesforce","Cisco","IBM","Oracle","AWS","Intuit","Adobe"]
companies_location = ["Los Angleles","San Luis Obispo","San Diego","San Jose","San Fransico, Cupertino","Santa Barbara","Sunnyvale"]

companies_date = ["June 2019","July 2019","Agust 2019","May 2019","May 2019 - June 2019","June 2019 - July 2019","June 2018 - July 2018","June 2018 - August 2018","August 2018"
                  ,"July 2018","June 2018","May 2018"]
companies_title = ["Software Developer","Software Engineer","Systems Software Developer","Web Developer","Computre Progrmamer"]
companies_description_front = ["Worked on creating a front end API. I was able to learn about full stack development."]
companies_description_back = ["Helped develop a large data base using mySQL. Learned how to create better code."]
companies_description_machine = ["Worked with neural nets. learned about the importance of stastical models"]
companies_description_security = ["Helped with the encryption of a file system. Learned a lot about algortythims and data structures."]
companies_description_graphics = ["Worked with realistic 3D modeling. Learned about implementing advanced physics engines"]
companies_description_low = ["Worked a lot with Linux enviroments. Helped develop a new Operating System"]

#clubs
months = ["Jan","Feb","Mar","Apr","May","Aug","June","October","Nov"]
years_4 = ["2017","2019","2018","2016"]
years_3 =["2017","2019","2018"]
years_2 = ["2019","2018"]
years_1 = ["2019"]

def student_major():
    return random.choice(major_list)

def student_projects(self):
    a = ()
    l = list(a)
    company_name = random.choice(companies_name)
    location = random.choice(companies_location)
    companiesdate = random.choice(companies_date)
    companies = random.choice(companies_title)
    if self.tech_skills == "Back end":
        company_desc = random.choice(companies_description_back)
    if self.tech_skills == "Front end":
        company_desc = random.choice(companies_description_front)
    if self.tech_skills == 'Graphics/Games':
        company_desc = random.choice(companies_description_graphics)
    if self.tech_skills == 'Low level':
        company_desc = random.choice(companies_description_low)
    if self.tech_skills == 'Security':
        company_desc = random.choice(companies_description_security)
    else:
        company_desc = random.choice(companies_description_machine)
    l.append(company_name)
    l.append(location)
    l.append(companiesdate)
    l.append(companies)
    l.append(company_desc)
    return l

def student_clubs(self):
    clubs = self.clubs





def resumegen(self):
    #major
    major = random.choice(major_list)
    education_start = 2020 - self.school


    # soft skills ex: ["Leadership", "Teamwork", "Learns quickly"]
    soft_skills = self.soft_skills

    # tech_skills ex: ["Python", "Javascript"]
    tech_skills = self.tech_skills


    # club title
    club = self.clubs
    #club year
    if self.school == 1:
         years_in_club = random.choice(years_1)
    if self.school == 2:
        years_in_club = random.choice(years_2)

    if self.school == 3:
        years_in_club = random.choice(years_3)
    else:
        years_in_club = random.choice(years_4)
    club_date = random.choice(months) + years_in_club
    #club title and date = ("Women in Software and Hardware", "October 2017 - Present")


    return club_date





