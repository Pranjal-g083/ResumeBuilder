from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import formset_factory
from django.contrib import messages
from django.forms.models import model_to_dict
# login required decorator
from django.contrib.auth.decorators import login_required
from .main import CreatePDF
# Create your views here.
def TemplatesView(request):
    return render(request, 'templates.html')
@login_required
def resumeView(request,pk):
    form=ResumeForm(request.POST or None)
    i=0
    if request.method == 'POST':
        if form.is_valid():
            obj=form.save(commit=False)
            request.session['resume_id']=obj.id
            obj.type=pk
            obj.author=request.user
            i=obj.id
            obj.save()
            return redirect('personal_info',obj.id)
        
    return render(request, 'resume.html', {'form':form, 'id':i})

@login_required
def PersonalInfoView(request, pk):
    # if there is already a personal info object for this resume, create a form with that object
    form=PersonalInfoForm()
    if Personal_Info.objects.filter(Resume=pk).exists():
        print("exists")
        # load the object having the details previously entered
        form = PersonalInfoForm(instance=Personal_Info.objects.get(Resume=pk))
    if request.method == 'POST':
        if Personal_Info.objects.filter(Resume=pk).exists():
            form = PersonalInfoForm(request.POST, request.FILES)
            if form.is_valid():
                obj=Personal_Info.objects.get(Resume=pk)
                obj.delete()
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
                return redirect('professional_summary', pk)
        else:
            form=PersonalInfoForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
                return redirect('professional_summary', pk)
    return render(request, 'personal_info.html', {'form': form})

@login_required
def ProfessionalSummaryView(request, pk):
    form=ProfessionalSummaryForm()
    if ProfessionalSummary.objects.filter(Resume=pk).exists():
        form=ProfessionalSummaryForm(instance=ProfessionalSummary.objects.get(Resume=pk))
    
    if request.method == 'POST':
        form = ProfessionalSummaryForm(request.POST)
        if form.is_valid():
            if ProfessionalSummary.objects.filter(Resume=pk).exists():
                obj=ProfessionalSummary.objects.get(Resume=pk)
                obj.delete()
            obj = form.save(commit=False)
            obj.Resume = Resume.objects.get(id=pk)
            obj.save()
            return redirect('skill_category', pk)
    return render(request, 'professional_summary.html', {'form':form})

@login_required
def EducationView(request,pk):
    EducationFormSet = formset_factory(EducationForm, extra=0, min_num=1, validate_min=True)
    
    formset = EducationFormSet(request.POST or None)
    forms=[]
    if Education.objects.filter(Resume=pk).exists():
        # load all the objects having the details previously entered
        education=Education.objects.filter(Resume=pk)
        for edu in education:
            forms.append(EducationForm(instance=edu))
        EducationFormSet = formset_factory(EducationForm, extra=0)
        formset= EducationFormSet(request.POST or None)
    if request.method == 'POST':
        # check if formset has atleast one form filled
        if formset.is_valid():
            if Education.objects.filter(Resume=pk).exists():
                Education.objects.filter(Resume=pk).delete()
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('project',pk)
        else:
            messages.error(request, 'Please fill atleast one form')
    return render(request, 'education.html', {'formset': formset, 'forms':forms})


@login_required
def ExperienceView(request, pk):
    ExperienceFormSet = formset_factory(ExperienceForm, extra=0)
    formset = ExperienceFormSet(request.POST or None)
    forms=[]
    if Experience.objects.filter(Resume=pk).exists():
        # load all the objects having the details previously entered
        experiences = Experience.objects.filter(Resume=pk)
        for experience in experiences:
            forms.append(ExperienceForm(instance=experience))
    if request.method == 'POST':
        if formset.is_valid():
            if Experience.objects.filter(Resume=pk).exists():
                Experience.objects.filter(Resume=pk).delete()
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('education', pk)
        else:
            print(formset.errors)
    return render(request, 'experience.html', {'formset': formset, 'forms':forms})



@login_required
def SkillCategoryView(request,pk):
    SkillFormSet=formset_factory(skillForm, extra=1)
    PreviousData={}
    if SkillCategory.objects.filter(Resume=pk).exists():
        skill_category=SkillCategory.objects.filter(Resume=pk)
        PreviousData['category']=[]
        i=0
        for skillcategory in skill_category:
            PreviousData['category'].append({'category':skillcategory.Name,'skills': []})
            for skil in skill.objects.filter(Category=skillcategory):
                PreviousData['category'][i]['skills'].append(skil.Name)
            i+=1
    if request.method == 'POST':
        skill_category_form=SkillCategoryForm(request.POST)
        formset=SkillFormSet(request.POST)
        if formset.is_valid() and skill_category_form.is_valid():
            skill_category=skill_category_form.save(commit=False)
            skill_category.Resume=Resume.objects.get(id=pk)
            skill_category.save()
            formset=SkillFormSet(request.POST)
            for form in formset:
                obj=form.save(commit=False)
                obj.Category=skill_category
                obj.save()
            
            return redirect('skill_category',pk)
    else:
        skill_category_form=SkillCategoryForm()
        formset=SkillFormSet()
    return render(request, 'skill_category.html', {'formset':formset, 'skill_category_form':skill_category_form, 'PreviousData':PreviousData, 'pk':pk})

@login_required
def ProjectView(request,pk):
    ProjectFormSet = formset_factory(ProjectForm, extra=0)
    formset=ProjectFormSet(request.POST or None)
    forms=[]
    if Project.objects.filter(Resume=pk).exists():
        for project in Project.objects.filter(Resume=pk):
            forms.append(ProjectForm(instance=project))
    if request.method == 'POST':
        if formset.is_valid():
            if Project.objects.filter(Resume=pk).exists():
                Project.objects.filter(Resume=pk).delete()
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('key_courses_category',pk)
    print(forms)
    return render(request, 'project.html', {'formset':formset, 'forms':forms})

@login_required
def KeyCoursesCategoryView(request,id):
    KeyCoursesFormSet = formset_factory(KeyCoursesForm, extra=0)
    PreviousData={}
    if KeyCoursesCategory.objects.filter(Resume=id).exists():
        key_courses_category=KeyCoursesCategory.objects.filter(Resume=id)
        PreviousData['category']=[]
        i=0
        for key_courses_category in key_courses_category:
            PreviousData['category'].append({'category':key_courses_category.Name,'courses': []})
            for course in KeyCourses.objects.filter(Category=key_courses_category):
                PreviousData['category'][i]['courses'].append(course.Name)
            i+=1
    if request.method == 'POST':
        Key_courses_category_form=KeyCoursesCategoryForm(request.POST)
        formset=KeyCoursesFormSet(request.POST)
        if formset.is_valid() and Key_courses_category_form.is_valid():
            key_courses_category=Key_courses_category_form.save(commit=False)
            key_courses_category.Resume=Resume.objects.get(id=id)
            key_courses_category.save()
            formset=KeyCoursesFormSet(request.POST)
            for form in formset:
                obj=form.save(commit=False)
                obj.Category=key_courses_category
                obj.save()
            return redirect('key_courses_category',id)
    else:
        key_courses_category_form=KeyCoursesCategoryForm()
        formset=KeyCoursesFormSet()
    return render(request, 'key_courses_category.html', {'formset':formset, 'key_courses_category_form':key_courses_category_form, 'PreviousData':PreviousData, 'pk':id})

@login_required
def PORView(request,pk):
    PorFormSet = formset_factory(Porform, extra=0)
    formset=PorFormSet(request.POST or None)
    forms=[]
    if PORs.objects.filter(Resume=pk).exists():
        for por in PORs.objects.filter(Resume=pk):
            forms.append(Porform(instance=por))
    if request.method == 'POST':
        
        if formset.is_valid():
            if PORs.objects.filter(Resume=pk).exists():
                PORs.objects.filter(Resume=pk).delete()
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('extra_curricular',pk)
    return render(request, 'por.html', {'formset':formset, 'forms':forms})

@login_required
def ExtraCurricularView(request,pk):
    ExtraCurricularFormSet = formset_factory(ExtraCurricularForm, extra=0)
    formset=ExtraCurricularFormSet(request.POST or None)
    forms=[]
    if ExtraCurricular.objects.filter(Resume=pk).exists():
        for extra in ExtraCurricular.objects.filter(Resume=pk):
            forms.append(ExtraCurricularForm(instance=extra))
    if request.method == 'POST':
        if ExtraCurricular.objects.filter(Resume=pk).exists():
            ExtraCurricular.objects.filter(Resume=pk).delete()
        if formset.is_valid():
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('achievements',pk)

    return render(request, 'extra_curricular.html', {'formset':formset, 'forms':forms})

@login_required
def AchievementView(request,pk):
    AchievementFormSet = formset_factory(AchievementForm, extra=0)
    formset=AchievementFormSet(request.POST or None)
    forms=[]
    if Achievements.objects.filter(Resume=pk).exists():
        for achievement in Achievements.objects.filter(Resume=pk):
            forms.append(AchievementForm(instance=achievement))
    if request.method == 'POST':
        if Achievements.objects.filter(Resume=pk).exists():
            Achievements.objects.filter(Resume=pk).delete()
        if formset.is_valid():
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj=form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('certifications',pk)
    
    return render(request, 'achievement.html', {'formset':formset, 'forms':forms})

@login_required
def CertificationView(request,pk):
    CertificationFormSet = formset_factory(CertificationForm, extra=0)
    formset=CertificationFormSet(request.POST or None)
    forms=[]
    if Certifications.objects.filter(Resume=pk).exists():
        for certification in Certifications.objects.filter(Resume=pk):
            forms.append(CertificationForm(instance=certification))
    if request.method == 'POST':
        if formset.is_valid():
            if Certifications.objects.filter(Resume=pk).exists():
                Certifications.objects.filter(Resume=pk).delete()
            for form in formset:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            for form in forms:
                obj = form.save(commit=False)
                obj.Resume = Resume.objects.get(id=pk)
                obj.save()
            return redirect('download',pk)
    return render(request, 'certification.html', {'formset':formset, 'forms':forms})

@login_required
def DownloadView(request,pk):
    # check if the resume's author is the current user
    if Resume.objects.get(id=pk).author != request.user:
        messages.info(request, 'You are not authorized to view this page')
        return redirect('home')
    ResumeData={}
    resume=Resume.objects.get(id=pk)
    ResumeData['Personal_Info']=model_to_dict(Personal_Info.objects.get(Resume=pk))
    ResumeData['Personal_Info']['Profile_Pic']='../'+ResumeData['Personal_Info']['Profile'].url
    ResumeData['ProfessionalSummary']=ProfessionalSummary.objects.get(Resume=pk).Summary
    ResumeData['Skills']=[]
    for skillCategory in SkillCategory.objects.filter(Resume=pk):
        ResumeData['Skills'].append({'SkillName':skillCategory.Name,'SkillSet':""})
        for skil in skill.objects.filter(Category=skillCategory):
            ResumeData['Skills'][-1]['SkillSet']=ResumeData['Skills'][-1]['SkillSet']+skil.Name+", "
        ResumeData['Skills'][-1]['SkillSet']=ResumeData['Skills'][-1]['SkillSet'][:-2]
    ResumeData['Experience']=[]
    for experience in Experience.objects.filter(Resume=pk):
        ResumeData['Experience'].append(model_to_dict(experience))
        ResumeData['Experience'][-1]['StartDate']=ResumeData['Experience'][-1]['Start'].strftime("%b %y")
        ResumeData['Experience'][-1]['EndDate']=ResumeData['Experience'][-1]['End'].strftime("%b %y")
        ResumeData['Experience'][-1]['WorkDone']=ResumeData['Experience'][-1]['Description']
    ResumeData['Education']=[]
    for education in Education.objects.filter(Resume=pk):
        ResumeData['Education'].append(model_to_dict(education))
        ResumeData['Education'][-1]['startYear']=ResumeData['Education'][-1]['Start'].strftime("%b %y")
        ResumeData['Education'][-1]['EndYear']=ResumeData['Education'][-1]['End'].strftime("%b %y")
    ResumeData['Projects']=[]
    for project in Project.objects.filter(Resume=pk):
        ResumeData['Projects'].append(model_to_dict(project))
        ResumeData['Projects'][-1]['StartDate']=ResumeData['Projects'][-1]['Start'].strftime("%b %y")
        ResumeData['Projects'][-1]['EndDate']=ResumeData['Projects'][-1]['End'].strftime("%b %y")
        ResumeData['Projects'][-1]['ProjectName']=ResumeData['Projects'][-1]['Name']
    ResumeData['KeyCourses']=[]
    for keyCourses in KeyCoursesCategory.objects.filter(Resume=pk):
        ResumeData['KeyCourses'].append({'Category':keyCourses.Name,'Courses':""})
        for course in KeyCourses.objects.filter(Category=keyCourses):
            ResumeData['KeyCourses'][-1]['Courses']=ResumeData['KeyCourses'][-1]['Courses']+course.Name+", "
        ResumeData['KeyCourses'][-1]['Courses']=ResumeData['KeyCourses'][-1]['Courses'][:-2]
    ResumeData['PORS']=[]
    for por in PORs.objects.filter(Resume=pk):
        ResumeData['PORS'].append(model_to_dict(por))
        ResumeData['PORS'][-1]['Organization']=ResumeData['PORS'][-1]['Club']
        ResumeData['PORS'][-1]['StartDate']=ResumeData['PORS'][-1]['Start'].strftime("%b %y")
        ResumeData['PORS'][-1]['EndDate']=ResumeData['PORS'][-1]['End'].strftime("%b %y")
    ResumeData['Extracurriculars']=[]
    for extra in ExtraCurricular.objects.filter(Resume=pk):
        ResumeData['Extracurriculars'].append(model_to_dict(extra))
        ResumeData['Extracurriculars'][-1]['Heading']=ResumeData['Extracurriculars'][-1]['Activity']
    ResumeData['Achievements']=[]
    for achievement in Achievements.objects.filter(Resume=pk):
        ResumeData['Achievements'].append(model_to_dict(achievement))
        ResumeData['Achievements'][-1]['Name']=ResumeData['Achievements'][-1]['Achievement']
        ResumeData['Achievements'][-1]['Date']=ResumeData['Achievements'][-1]['Date'].strftime("%b %y")
    ResumeData['Certifications']=[]
    for certification in Certifications.objects.filter(Resume=pk):
        ResumeData['Certifications'].append(model_to_dict(certification))
    CreatePDF(resume.type,resume.name+str(resume.id),ResumeData)
    context={
        'pk':pk,
        'name': 'assets/img/Template'+str(resume.type)+'.png',
        'pdf':'assets/'+resume.name+str(resume.id)+'.pdf',
        'tex': 'assets/'+resume.name+str(resume.id)+'.tex',
        'Name':resume.name
    }
    return render(request, 'download.html', context)

@login_required
def works(request):
    # get all the resumes of the current user
    resumes=Resume.objects.filter(author=request.user)
    data={}
    data['resumes']=[]
    for resume in resumes:
        data['resumes'].append(model_to_dict(resume))
        data['resumes'][-1]['type']='assets/img/Template'+str(data['resumes'][-1]['type'])+'.png'
    return render(request, 'works.html', {'data':data})

def handler404(request, exception):
    return render(request, '404.html', status=404)