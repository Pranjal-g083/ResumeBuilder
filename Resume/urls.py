from django.urls import path, include
from .views import *
urlpatterns = [
    path('templates/', TemplatesView, name='templates'),
    path('personal_info/', PersonalInfoView, name='personal_info'),
    path('professional_summary/', ProfessionalSummaryView, name='professional_summary'),
    path('education/', EducationView, name='education'),
    path('education_form/', EducationView_Form, name='education_form'),
    path('experience/', ExperienceView, name='experience'),
    path('experience_form/', ExperienceView_Form, name='experience_form'),
    path('skill_category/', SkillCategoryView, name='skill_category'),
    path('skill_category_form/', SkillCategoryView_Form, name='skill_category_form'),
    path('skill_form/', SkillView_Form, name='skill_form'),
]
