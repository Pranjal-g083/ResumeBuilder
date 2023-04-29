from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def TemplatesView(request):
    return render(request, 'templates.html')

def PersonalInfoView(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education')
    else:
        form = PersonalInfoForm()
    return render(request, 'personal_info.html', {'form':form})

def ProfessionalSummaryView(request):
    if request.method == 'POST':
        form = ProfessionalSummaryForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('education')
    else:
        form = ProfessionalSummaryForm()
    return render(request, 'professional_summary.html', {'form':form})

def EducationView(request):
    form = EducationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('education')
    return render(request, 'education.html', {'form':form})

def EducationView_Form(request):
    return render(request, 'education_form.html', {'form': EducationForm()})

def ExperienceView(request):
    form=ExperienceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('experience')
    return render(request, 'experience.html', {'form':form})

def ExperienceView_Form(request):
    return render(request, 'experience_form.html', {'form':ExperienceForm()})

def SkillCategoryView(request):
    form=SkillCategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('skill_category')
    request.session['i'] = 0
    return render(request, 'skill_category.html', {'form':form})

def SkillCategoryView_Form(request):
    form = skillForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('skill_category')
    else:
        # Get the current value of i from the session or default to 0
        i = request.session.get('i', 0)
        # Increment i by 1
        i += 1
        # Save the new value of i in the session
        request.session['i'] = i
    return render(request, 'skill_category_form.html', {'form': SkillCategoryForm(), 'id': request.session['i']})


def SkillView_Form(request):
    return render(request, 'skill_form.html', {'form':skillForm()})

def ProjectView(request):
    form=ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('project')
    return render(request, 'project.html', {'form':form})

def ProjectView_Form(request):
    return render(request, 'project_form.html', {'form':ProjectForm()})

def KeyCoursesCategoryView(request):
    form=KeyCoursesCategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('key_courses_category')
    request.session['key'] = 0
    return render(request, 'key_courses_category.html', {'form':form})

def KeyCoursesCategoryView_Form(request):
    form = KeyCoursesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('key_courses_category')
    else:
        # Get the current value of i from the session or default to 0
        key = request.session.get('key', 0)
        # Increment i by 1
        key += 1
        # Save the new value of i in the session
        request.session['key'] = key
    return render(request, 'key_courses_category_form.html', {'form': KeyCoursesCategoryForm(), 'id': request.session['key']})

def KeyCoursesView_Form(request):
    return render(request, 'key_courses_form.html', {'form':KeyCoursesForm()})

def PORView(request):
    form=Porform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('por')
    return render(request, 'por.html', {'form':form})

def PORView_Form(request):
    return render(request, 'por_form.html', {'form':Porform()})

def ExtraCurricularView(request):
    form=ExtraCurricularForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('extra_curricular')
    return render(request, 'extra_curricular.html', {'form':form})

def ExtraCurricularView_Form(request):
    return render(request, 'extra_curricular_form.html', {'form':ExtraCurricularForm()})

def AchievementView(request):
    form=AchievementForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('achievement')
    return render(request, 'achievement.html', {'form':form})

def AchievementView_Form(request):
    return render(request, 'achievement_form.html', {'form':AchievementForm()})

def CertificationView(request):
    form=CertificationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('certification')
    return render(request, 'certification.html', {'form':form})

def CertificationView_Form(request):
    return render(request, 'certification_form.html', {'form':CertificationForm()})

def DownloadView(request):
    return render(request, 'download.html')