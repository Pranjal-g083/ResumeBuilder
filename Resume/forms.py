from .models import *
from django import forms


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Personal_Info
        fields = (
            'Name',
            'Email',
            'Phone',
            'Profile',
            'Github',
            'Website',
            'Linkedin',
            'Address',
        )
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = (
            'Degree',
            'Field',
            'Institute',
            'CGPA',
            'Start',
            'End'
        )
        widgets={
            'Start':forms.DateInput(attrs={'type':'date'}),
            'End':forms.DateInput(attrs={'type':'date'}),
        }
        
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = (
            'Company',
            'Position',
            'Start',
            'End',
            'Description'
        )
        widgets={
            'Start':forms.DateInput(attrs={'type':'date'}),
            'End':forms.DateInput(attrs={'type':'date'}),
        }
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'Name',
            'Start',
            'End',
            'Description',
            'code',
            'link'
        )
        widgets={
            'Start':forms.DateInput(attrs={'type':'date'}),
            'End':forms.DateInput(attrs={'type':'date'}),
        }
        
class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = (
            'Name',
        )
        labels={
            'Name':'Category Name'
        }
        
class skillForm(forms.ModelForm):
    class Meta:
        model = skill
        fields = (
            'Name',
        )
        labels={
            'Name':'Skill'
        }
        
class KeyCoursesCategoryForm(forms.ModelForm):
    class Meta:
        model = KeyCoursesCategory
        fields = (
            'Name',
        )
        
class KeyCoursesForm(forms.ModelForm):
    class Meta:
        model = KeyCourses
        fields = (
            'Name',
        )
        
class Porform(forms.ModelForm):
    class Meta:
        model = PORs
        fields = (
            'Club',
            'Position',
            'Start',
            'End',
            'Description'
        )
        widgets={
            'Start':forms.DateInput(attrs={'type':'date'}),
            'End':forms.DateInput(attrs={'type':'date'}),
        }
        
class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields = (
            'Achievement',
            'Event',
            'Date'
        )
        widgets={
            'Date':forms.DateInput(attrs={'type':'date'}),
        }
        
class ProfessionalSummaryForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSummary
        fields = (
            'Summary',
        )
        
class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = (
            'Certificate',
            'CertifiedBy'
        )
        
class ExtraCurricularForm(forms.ModelForm):
    class Meta:
        model = ExtraCurricular
        fields = (
            'Activity',
            'Description'
        )