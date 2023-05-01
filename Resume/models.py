from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_summary_length(value):
    """
    Validator function to check that the 'summary' field has at least 10 words.
    """
    word_count = len(value.split())
    if word_count < 10:
        raise ValidationError(
            _('The summary must have at least 10 words.'),
            code='invalid'
        )

class Resume(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=False, null=False)
    type=models.IntegerField(default=1)
    def __str__(self):
        return self.author.username

class Personal_Info(models.Model):
    Name = models.CharField(max_length=100, blank=False, null=False)
    Email = models.EmailField(max_length=100, blank=False, null=False)
    # phone number is 10 digit 
    Phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{1,10}$', message='Only digits are allowed', code='nomatch'),MinLengthValidator(10)], blank=False, null=False)
    Profile=models.ImageField(upload_to='images/',default='images/default.jpg')
    Github=models.CharField(max_length=100, blank=True, null=True)
    Website=models.CharField(max_length=100, blank=True, null=True)
    Linkedin=models.CharField(max_length=100, blank=True, null=True)
    Address=models.CharField(max_length=100, blank=False, null=False, default='Delhi')
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Name
    
class Education(models.Model):
    # Degree is an enum of B.Tech M.tech M.Sc P.hd M.S.R. Senior Secondary Secondary
    degree_options = [ ('B.Tech', 'B.Tech'), ('M.tech', 'M.tech'), ('M.Sc', 'M.Sc'), ('P.hd', 'P.hd'), ('M.S.R.', 'M.S.R.'), ('Senior Secondary', 'Senior Secondary'), ('Secondary', 'Secondary') ]
    Degree=models.CharField(max_length=30, choices=degree_options, default=None)
    Field=models.CharField(max_length=100, blank=False, null=False)
    Institute=models.CharField(max_length=100, blank=False, null=False)
    CGPA=models.FloatField(blank=False, null=False)
    Start=models.DateField(blank=False, null=False)
    End=models.DateField(blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Field
    
class Experience(models.Model):
    Company=models.CharField(max_length=100, blank=False, null=False)
    Position=models.CharField(max_length=100, blank=False, null=False)
    Start=models.DateField(blank=False, null=False)
    End=models.DateField(blank=False, null=False)
    Description=models.TextField(blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Position
    
class Project(models.Model):
    Name=models.CharField(max_length=100, blank=False, null=False)
    Start=models.DateField(blank=False, null=False)
    End=models.DateField(blank=False, null=False)
    Description=models.TextField(blank=False, null=False)
    code=models.URLField(blank=False, null=False)
    link=models.URLField(blank=True, null=True)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Name
    
class SkillCategory(models.Model):
    Name=models.CharField(max_length=100, blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Name
    
class skill(models.Model):
    Name=models.CharField(max_length=30, blank=False, null=False, validators=[MaxLengthValidator(30)])
    Category=models.ForeignKey(SkillCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name

class KeyCoursesCategory(models.Model):
    Name=models.CharField(max_length=100, blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Name
    
class KeyCourses(models.Model):
    Name=models.CharField(max_length=100, blank=False, null=False)
    Category=models.ForeignKey(KeyCoursesCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    
class PORs(models.Model):
    Club=models.CharField(max_length=100, blank=False, null=False)
    Position=models.CharField(max_length=100, blank=False, null=False)
    Start=models.DateField(blank=False, null=False)
    End=models.DateField(blank=False, null=False)
    Description=models.TextField(blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Position
    
class Achievements(models.Model):
    Achievement=models.TextField(blank=False, null=False)
    Event=models.CharField(max_length=100, blank=False, null=False)
    Date=models.DateField(blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Event
    
class ProfessionalSummary(models.Model):
    Summary=models.TextField(blank=False, null=False, validators=[validate_summary_length])
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Summary
    
class Certifications(models.Model):
    Certificate=models.TextField(blank=False, null=False)
    CertifiedBy=models.CharField(max_length=100, blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Certificate

class ExtraCurricular(models.Model):
    Activity=models.CharField(max_length=100, blank=False, null=False)
    Description=models.TextField(blank=False, null=False)
    Resume=models.ForeignKey(Resume,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Activity