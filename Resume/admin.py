from django.contrib import admin
from .models import ( 
    Personal_Info, 
    Education, 
    Resume, 
    Experience, 
    Project, 
    SkillCategory, 
    skill,
    KeyCoursesCategory,
    KeyCourses,
    PORs,
    Achievements,
    ProfessionalSummary,
    Certifications,
    ExtraCurricular,
)
# Register your models here.
admin.site.register(Personal_Info)
admin.site.register(Education)
admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Project)


class SkillAdmin(admin.TabularInline):
    model=skill

class SkillCategoryAdmin(admin.ModelAdmin):
    inlines=[SkillAdmin]
    
admin.site.register(SkillCategory, SkillCategoryAdmin)

class KeyCoursesAdmin(admin.TabularInline):
    model=KeyCourses
    
class KeyCoursesCategoryAdmin(admin.ModelAdmin):
    inlines=[KeyCoursesAdmin]
    
admin.site.register(KeyCoursesCategory, KeyCoursesCategoryAdmin)
admin.site.register(PORs)
admin.site.register(Achievements)
admin.site.register(ProfessionalSummary)
admin.site.register(Certifications)
admin.site.register(ExtraCurricular)