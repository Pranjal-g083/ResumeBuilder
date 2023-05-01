# Resume Builder Website
![logo](images/resume.png)
> A website where you can make and edit you resumes without going through cumbersome latex files.

## Table of Contents
- [Resume Builder Website](#resume-builder-website)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
    - [Key Features](#key-features)
    - [Tech Stack](#tech-stack)
  - [Data Flow Diagram](#data-flow-diagram)
    - [Database](#database)
    - [Overall Flow](#overall-flow)
    - [Login Flow](#login-flow)
    - [Resume Form](#resume-form)
  - [Demo](#demo)
    - [Home Page](#home-page)
    - [Login](#login)
    - [Resume Builder](#resume-builder)
    - [Downloads Page](#downloads-page)
    - [Example resume in pdf format](#example-resume-in-pdf-format)
    - [My Works Page](#my-works-page)
  - [Instructions](#instructions)
  - [References](#references)
  - [Author Info](#author-info)
    - [Akshat Mittal](#akshat-mittal)
    - [Dhananjai](#dhananjai)
    - [Pranjal Baranwal](#pranjal-baranwal)
    - [Satvik Tiwari](#satvik-tiwari)
    - [Ujwal Kumar](#ujwal-kumar)
---
## Description
The website offers a basic form to create resumes which can be later downloaded in latex or pdf format.

The resumes can also be edited later.

### Key Features
- A basic form for Resume Details.
- Option to download files later as pdf or latex.
- Option to Sign in to save your work and edit them later.
- Three Authentication types
    * Basic authentication with username,email and password
    * Authentication with third party sites
        * Google
        * Office 365 (Using IITG credentials)
- A dedicated `Works` page for downloading and editing your resumes later.

### Tech Stack
- Frontend: HTML, CSS, Bootstrap, Javascript
- Backend: Django (+ allauth, crispy_forms, pillow, Cheetah3 and other python libraries), SQLite(inbuilt in django)
- Latex: pdflatex, texlive

[Back To The Top](#resume-builder-website)

---
## Data Flow Diagram

### Database

![database](images/Database.jpg)
### Overall Flow

![overall](images/OverallFlow.jpg)
### Login Flow
![login](images/Login.jpg)

### Resume Form
![form](images/ResumeForm.jpg)

### Generate Resume
![generate](images/GeneratingPDF.jpg)
---

## Demo
After running the localhost using the [instructions](#instructions) specified later, go to the following [url](http://localhost:8000).

### Home Page
The home page will look like this:
![home](images/HomePage.jpeg)
### Login
Go to the Login page, it will look like this:
![login](images/LoginPage.jpeg)
Login with google:
![google](images/GoogleLoginRedirect.jpeg)
After logging in, you will be redirected to the home page with success message
![success](images/SuccessLoginGmail.jpeg)
Login with Office 365:
![office](images/MicrosoftLoginRedirect.jpeg)
After logging in, you will be redirected to the home page with success message
![success](images/SuccessLoginMicrosoft.jpeg)
Register with username and password:
![username](images/SignupWithEmailPage.jpeg)
After registering, you will be redirected to the login Page

After Logging in with any of the three methods, you will be redirected to the home page with a success message.

### Resume Builder
On clicking the Build Resume button, you will be redirected to the template Selection Page:
![template](images/TemplateSelectionPage.jpeg)
Click on  the desired template, you will be redirected to the form page:
Name the Resume:
![name](images/AddResumeName.jpeg)
Click on Save, you will be redirected to the Personal Info page:
![personal](images/AddPersonalDetail.jpeg)
CLick on Save, you will be redirected to the Add your Technical summary page:
![technical](images/AddSummary.jpeg)
Click on Save, you will be redirected to the Add your Skills page:
![skills](images/AddSkill.jpeg)
![skills](images/AddSkill2.jpeg)
Click on Save, you will be redirected to the Add your Experience page:
![experience](images/AddExperience.jpeg)
Click on Save, you will be redirected to the Add your Education page:
![education](images/AddEducation.jpeg)
Click on Save, you will be redirected to the Add your Projects page:
![projects](images/AddProjects.jpeg)
Click on Save, you will be redirected to the Add your Courses page:
![courses](images/AddCourses.jpeg)
![courses](images/AddCourses2.jpeg)
Click on Save, you will be redirected to the Add your POR page:
![por](images/AddPOR.jpeg)
Click on Save, you will be redirected to the Add your Achievements page:
![achievements](images/AddAchievements.jpeg)
Click on Save, you will be redirected to the Add your ExtraCurricular Activities page:
![extra](images/AddExtraCurricular.jpeg)
Click on Save, you will be redirected to the Add your Certificates page:
![certificates](images/AddCertificates.jpeg)

### Downloads Page
After adding all the details, click on the Finish button, you will be redirected to the Downloads page:
![download](images/ViewResume.jpeg)
On Clicking the Edit Resume option, you will be redirected to the Personal Info Form Page with prefiled details.
![edit](images/EditResume.jpeg)

### Example resume in pdf format
On Clicking the download pdf option, you will be redirected to the pdf File Viewer of the Browswer:
![pdf](images/DownloadResume.png)
On Clicking the download latex option, a latex file will be downloaded in your machine.


### My Works Page
In the My Works Page, you can view all your resumes:
![works](images/MyWorks.jpeg)


[Back To The Top](#resume-builder-website)


---
## Instructions
1. First create a virtual environment using the following command:
    ```bash
    python3 -m venv env
    ```
2. Activate the virtual environment using the following command:
    ```bash
    source env/bin/activate
    ```
3. Install all the dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```
4. Download the texlive package using the following command:
  * For Linux
    ```bash
    sudo apt-get install texlive-full
    ```
  * For Windows Download the texlive package from [here](https://www.tug.org/texlive/acquire-netinstall.html)
    and install it.
  
  * For Mac
    ```bash
    brew cask install mactex
    ```

5. Run the following command to start the server:
    ```bash
    python manage.py runserver
    ```

6. Go to the following [url](http://localhost:8000) to view the website.

  
[Back To The Top](#resume-builder-website)

---
## References
- Django: [Django Documentation](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
- BootStrap: [BootStrap Documentation](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- Allauth: [Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/installation.html)
- Cheetah3: [Cheetah3 Documentation](https://cheetahtemplate.org/docs/users_guide_html_multipage/index.html)
- Texlive: [Texlive Documentation](https://www.tug.org/texlive/doc/texlive-en/texlive-en.html)
- Overleaf Templates:
    - Template 1: [Template 1](https://www.overleaf.com/latex/templates/altacv-nicolasomar-fork/htfpmrwhbwpw)
    - Template 2: [Template 2](https://www.overleaf.com/latex/templates/resume-template-by-krishna-priyatham-potluri/cykhvmybxmjz)
    - Template 3: See `Template3` folder in the repository
    - IITG Template: [IITG Template](https://www.overleaf.com/latex/templates/iit-guwahati-resume/fvqtppmzhvxn)
- Google Authentication: [Google Authentication](https://django-allauth.readthedocs.io/en/latest/providers.html#google)
- Office 365 Authentication: [Office 365 Authentication](https://django-allauth.readthedocs.io/en/latest/providers.html#microsoft-graph)
- Formsets: [Formsets](https://docs.djangoproject.com/en/4.0/topics/forms/formsets/)

[Back To The Top](#resume-builder-website)

---
## Author Info

### Akshat Mittal
- Email - [m.akshat@iitg.ac.in](mailto:m.akshat@iitg.ac.in)
- Github - [akshatmittal2002](https://github.com/akshatmittal2002)
- Roll Number - 200101011

### Dhananjai
- Email - [d.dhananjai@iitg.ac.in](mailto:d.dhananjai@iitg.ac.in)
- Github - [DestinyWarrior](https://github.com/DestinyWarrior)
- Roll Number - 200101029

### Pranjal Baranwal
- Email - [pranjal.baranwal@iitg.ac.in](mailto:pranjal.baranwal@iitg.ac.in)
- Github - [Pranjal-g083](https://github.com/Pranjal-g083)
- Roll Number - 200101083

### Satvik Tiwari
- Email - [t.satvik@iitg.ac.in](mailto:t.satvik@iitg.ac.in)
- Github - [stanptown](https://github.com/stanptown)
- Roll Number - 200101091

### Ujwal Kumar
- Email - [k.ujwal@iitg.ac.in](mailto:k.ujwal@iitg.ac.in)
- Github - [ujwal-k03](https://github.com/ujwal-k03)
- Roll Number - 200101100

[Back To The Top](#resume-builder-website)