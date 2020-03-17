import random

major_list = ["Software Engineering","Computer Science"]



projects_front_4 = [("Movie Search App","Building this application I learned "
            "React Skills using the relatively new "
            "Hooks API. The example projects makes use of React components and CSS styling."),
            ("Chat App","The project shows how to setup a Vue app from scratch, creating components, handling state, creating route, connecting to a third party service and even handling authentication."),
            ("Weather App","Project implements Firebase, CSS with Grid Layout and Flexbox to create a ploshied product."),
            ("Re-create Giphy","a web app which uses a search input and Giphy’s API to display giphs on a page. Used JavaScript and jQuery.")]
projects_low_4 = [("Custom Operating System","Built an operating system from scratch. Learned about Linux as a development environment and x86 assembly in-depth."),
                    ("Pipelining", "Built a pipleline in C to send messages from a parent to a child. The message got mutated along the way to demonstrate correct setup of the pipes."),
                    ("Raspberry Pi Robot", "Built a basic operating system using assembly to control a small robot")]
projects_back_4 = [("FTP Client","Built a FTP client that supports secure file transfer"),
                    ("Sports Page","Uses a  automatically updating data set. Learned about web scraping and web input to CSV output"),
                    ("Database Migration", "Migrated information from a MySQL database to a Cassandra database without loss of data. Ensured data security during migration")]
projects_graphics_4 = [("Procedurally Generated Map Maker","Browser-based application that allows users to procedurally generate a terrain map based on a random seed."),
                        ("Pixel art generator","Built a tool that takes an image as input and samples the image to produce pixel art as output. Learned about CSS and Pylatex.")]
projects_Machine_4 = [("Niche Chatbot","Used NLP to create a chatbot that can talk about any topic it can scrape from wikipeda "),
                        ("Spam Classifier","Uses content of email to detect Spam or Non Spam emails. Learned about NLP and Neural Nets."),
                        ("Shark Identification", "Used transfer learning and machine vision to identify sharks in the water and to distinguish them from surfers or other objects."),
                        ("Backpropagation", "Implemented backpropagation from scratch to learn about the inner workings of a neural network")]
projects_Security_4 = [("Privileged access management","Covers human and non-human system accounts and supports a combination of on-premises, cloud, and hybrid environments, as well as APIs for automation."),
                        ("Reputation Server","Able to track a users behavior based on feed back. Learned about SQL"),
                        ("Firewall","Created a secure and dynamic firewall using C++ learned a lot about algorithms")]


#work experience
companies_name = ["Amazon","Google","Apple","Microsoft","Workday","Salesforce","Cisco","IBM","Oracle","AWS","Intuit","Adobe"]
companies_location = ["Los Angleles","San Luis Obispo","San Diego","San Jose","San Fransico, Cupertino","Santa Barbara","Sunnyvale"]

companies_date = ["June 2019","July 2019","Agust 2019","May 2019","May 2019 - June 2019","June 2019 - July 2019","June 2018 - July 2018","June 2018 - August 2018","August 2018"
                  ,"July 2018","June 2018","May 2018"]
companies_title = ["Software Developer","Software Engineer","Systems Software Developer","Web Developer","Computer Programmer"]
companies_description_front = ["Worked on creating a front end API. I was able to learn about full stack development.", 
                                "Helped devlop and design a new user UI. I gained a lot of design experience.",
                                "Redesigned my team's internally facing page. Other teams use our portal in order to file bug tickets and request important changes. Focus was on ease of use and an attractive design."]
companies_description_back = ["Helped develop a large data base using mySQL. Learned how to create more optimized code to process large amounts of data at once.", 
                                "Was a part of a team that developed an self updating database. I was able to streghten my skills in MySQL and Ruby on Rails.",
                                "Redesigned the database that supports my team's data analysis system. Optimized the queries for faster data access and to work on a large scale distributed system."]
companies_description_machine = ["Employed a machine learning algorithm to sort user feedback and process it. Reduced the amount of human hours needed to examine feedback by one third.",
                                    "Developed an algorithm to identify the health of a user's garden plant using machine learning. This was a critical feature in the most recent sofware update of my company's app."]
companies_description_security = ["Helped with the encryption of a file system. Over the course of this projet, I learned a lot about algorithms and data structures.",
                                    "Deployed a full web security system for a new branch of my team's internal website. Built on top of existing security systems as well as employed cutting edge web security methods."
                                    "Collaborated with my company's user privacy team to find holes in the existing security system. Proposed patches to the security risks that I exposed through whitehat methods."]
companies_description_graphics = ["Worked with realistic 3D modeling. Learned about implementing advanced physics engines", 
                                    "Used Godot to develop a 2D platformer game. From my time working on the project I was able to learn game design, texture mapping, and game physics",
                                    "Designed and implemented graphics for a short animated film. Our film won top place in the Khem Animation Film Festival for animation style."]
companies_description_low = ["Worked heavily with Linux enviroments. Helped streamline the Operating System for one of our company's unreleased devices", 
                                "Worked with linux to devolp a smart and adaptive firewall.",
                                "Adapted my team's pipelining process in order to improve efficiency. Worked with large amounts of legacy code to ensure no data leakage occurred."]

#clubs
months = ["Jan","Feb","Mar","Apr","May","Aug","June","October","Nov"]
years_4 = ["2017","2019","2018","2016"]
years_3 =["2017","2019","2018"]
years_2 = ["2019","2018"]
years_1 = ["2019"]

#skillsets
front_end_skills = ["HTML","CSS","JavaScript","jQuery","JavaScript Framework","Git/Version Control", "APIs"]
back_end_skills = ["service architecture","design patterns","web-frameworks","technical documentation","Databases","SQLite","MySQL"]
low_level_skills = ["C","Assembly language","Perl","Linux","Unix","Databases","C++"]
machine_skills = ["Python","C++",'Java',"Statistics","Data Modeling"," Algorithms","Distributed Computing"]
graphics_skills = ["C#","C++","Algorithms","Java","Javascripy","HTML","CSS"]
security_skills = ["C++","C","Cloud computing","Angular JS","Node.js","Blackbox testing","HTML"]



def student_major():
    return random.choice(major_list)

def student_work(student):
    a = ()
    b = ()
    l = list(a)
    m = list(b)
    company_name = random.choices(companies_name, k=2)
    location = random.choices(companies_location, k=2)
    companiesdate = random.choices(companies_date, k=2)
    companies = random.choices(companies_title, k=2)
    if student.specialization == "Back end":
        company_desc = random.choices(companies_description_back, k=2)
    elif student.specialization == "Front end":
        company_desc = random.choices(companies_description_front, k=2)
    elif student.specialization == 'Graphics/Games':
        company_desc = random.choices(companies_description_graphics, k=2)
    elif student.specialization == 'Low level':
        company_desc = random.choices(companies_description_low, k=2)
    elif student.specialization == 'Security':
        company_desc = random.choices(companies_description_security, k=2)
    else:
        company_desc = random.choices(companies_description_machine, k=2)
    l.append(company_name[0] + " - " + location[0])
    l.append(companiesdate[0])
    l.append(companies[0])
    l.append(company_desc[0])
    m.append(company_name[1] + " - " + location[1])
    m.append(companiesdate[1])
    m.append(companies[1])
    m.append(company_desc[1])
    return [tuple(l), tuple(m)]



def student_proj(student):
    if student.specialization == "Back end":
        proj_desc = random.choice(projects_back_4)
    elif student.specialization == "Front end":
        proj_desc = random.choice(projects_front_4)
    elif student.specialization == 'Graphics/Games':
        proj_desc = random.choice(projects_graphics_4)
    elif student.specialization == 'Low level':
        proj_desc = random.choice(projects_low_4)
    elif student.specialization == 'Security':
        proj_desc = random.choice(projects_Security_4)
    else:
        proj_desc = random.choice(companies_description_machine)
    return proj_desc

def student_hard(student):
    if student.specialization == "Back end":
        skill_desc = random.choices(back_end_skills, k = 3)
    elif student.specialization == "Front end":
        skill_desc = random.choices(front_end_skills, k = 3)
    elif student.specialization == 'Graphics/Games':
        skill_desc = random.choices(graphics_skills, k =3)
    elif student.specialization == 'Low level':
        skill_desc = random.choices(low_level_skills, k = 3)
    elif student.specialization == 'Security':
        skill_desc = random.choices(security_skills, k = 3)
    else:
        skill_desc = random.choices(machine_skills, k = 3)
    return skill_desc










