from Cheetah.Template import Template
import os
import shutil

dict={
    "Personal_Info":{
        "Name":"Pranjal Baranwal",
        "Profile_Pic": "pranjal.jpg",
        "Phone": "+91 1234567890",
        "Email": "pranjalbaranwal334@outlook.com",
        "Github": "Pranjal-g083",
        "Website": "https://Pranjal-g083.github.io",
        "Linkedin": "pranjal-baranwal-850210203",
        "Address": "Delhi, India"
    },
    "Education": [
        {
            "Degree":"B.Tech Major",
            "Field": "Computer Science and Engineering",
            "Institute":"Indian Institute of Technology, Guwahati",
            "CGPA":"8.40",
            "startYear":"2020",
            "EndYear":"Present"
        },
        {
            "Degree":"Senior Secondary",
            "Institute":"CBSE Board",
            "Field": "PCM with Computer Science",
            "CGPA":"92\%",
            "startYear":"2017",
            "EndYear":"2019"
        },
        {
            "Degree":"Secondary",
            "Institute":"CBSE Board",
            "Field": "PCM with Computer Science",
            "CGPA":"92\%",
            "startYear":"2017",
            "EndYear":"2019"
        }
    ],
    "Experience":[
        {
            "Company":"Sprinklr",
            "Position":"Product Engineer Intern",
            "StartDate":"22 May 2023",
            "EndDate":"15 July 2023",
            "WorkDone":"Developed a feature to enable users to create and manage their own custom dashboards. Created an authentication system for the feature using OAuth 2.0."
        }
    ],
    "Projects":[
        {
            "ProjectName":"Movie Review Site",
            "StartDate":"May. 2022",
            "EndDate":"June. 2022",
            "Description":[
                "Developed a Django based website to rate, review and receive recommendations on movies using tmdb api.",
                "Key features include email verification and google authentication, movie recommendations, replies to comments, dedicated user page with recent actions and favourites tab."
            ],
            "link":"https://movrev.pythonanywhere.com/",
            "code": "https://github.com/Pranjal-g083/Boomorev"
        }
    ],
    "Skills":[
        {
            "SkillName":"Programming Languages",
            "SkillSet":"C, C++, Python, Java, JavaScript, HTML, CSS, SQL"
        },
        {
            "SkillName":"Frameworks",
            "SkillSet":"Django, React, Node.js, Express.js, Bootstrap, Materialize, jQuery"
        },
        {
            "SkillName":"Tools",
            "SkillSet":"Git, GitHub, VS Code, Jupyter Notebook, PyCharm, Android Studio, Microsoft Office"
        },
        {
            "SkillName":"Operating Systems",
            "SkillSet":"Windows, Linux"
        }
    ],
    "KeyCourses":[
        {
            "Category":"Computer Science",
            "Courses": "Computer Networks, Operating Systems, Formal Languages and Automata theory, Data Structures, Algorithms, Digital Design, Computer Organisation and Architecture, Database Management systems"
        },
        {
            "Category":"Mathematics",
            "Courses":"Probability and Statistics, Linear Algebra, Calculus, Discrete Mathematics, Differential Equations"
        }
    ],
    "PORS":[
        {
            "Organization": "Coding Club",
            "Position": "Secretary",
            "StartDate": "May. 2022",
            "EndDate": "March. 2023",
        }
    ],
    "Achievements":[
        {
            "Name": "All India Rank 519",
            "Event": "JEE Advanced",
            "Date": "2020",
        }
    ],
    "ProfessionalSummary": "I majorly like problem solving and hence I practice Competitive programming. I am also exploring development using web technologies like django and mobile technologies like flutter. My hobbies include playing badminton, watching anime and gaming.",
    "Certifications":[
        {
            "Certificate": "Python for Everybody",
            "CertifiedBy": "University of Michigan",
        }
    ],
    "Extracurriculars":[
        {
            "Heading": "Kriti Startup Sprint 2023",
            "Description": "Developed a web app to help people gain rewards by participating in different kind of competitions."
        },
        {
            "Heading": "Sahyog 2023",
            "Description":"Developed a web app to manage previous year notes and resources and library books."
        }
    ]
}

def CreatePDF(template_type, output_name, dict):
    file_dir = os.path.join(os.getcwd(), f'Template{template_type}\\')
    file_name = os.path.join(file_dir, 'template.tex')
    out_file_name = os.path.join(file_dir, 'output.tex')

    with open(file_name, 'r') as f:
        template_str = f.read()

    # preprocess skills
    for el in dict["Skills"]:
        el["SkillSetCommas"] = el["SkillSet"]
        el["SkillSet"] = el["SkillSet"].split(", ")

    # preprocess courses
    for el in dict["KeyCourses"]:
        el["CourseCommas"] = el["Courses"]
        el["Courses"] = el["Courses"].split(", ")

    # preprocess workdone
    for el in dict["Experience"]:
        el["WorkDoneSplit"] = el["WorkDone"].split(". ")

    template = Template(template_str, searchList=[dict])
    template = template.__str__()

    with open(out_file_name, 'w') as f:
        f.write(template)
    
    os.chdir(file_dir)
    os.system(f'pdflatex -interaction=batchmode output.tex' )
    os.rename(os.path.join(file_dir, 'output.pdf'), os.path.join(file_dir, output_name))
    shutil.copy(os.path.join(file_dir, output_name), os.path.join(file_dir, '../', output_name))
    
    
CreatePDF(1, 'jjj.pdf', dict)