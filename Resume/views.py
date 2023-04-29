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