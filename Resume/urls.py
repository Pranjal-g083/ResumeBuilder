from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('templates/', TemplatesView, name='templates'),
    path('personal_info/<int:pk>', PersonalInfoView, name='personal_info'),
    path('professional_summary/<int:pk>', ProfessionalSummaryView, name='professional_summary'),
    path('education/<int:pk>', EducationView, name='education'),
    path('experience/<int:pk>', ExperienceView, name='experience'),
    path('skill_category/<int:pk>', SkillCategoryView, name='skill_category'),
    path('project/<int:pk>', ProjectView, name='project'),
    path('key_courses_category/<int:id>', KeyCoursesCategoryView, name='key_courses_category'),
    path('pors/<int:pk>', PORView, name='pors'),
    path('extra_curricular/<int:pk>', ExtraCurricularView, name='extra_curricular'),
    path('Achievement/<int:pk>', AchievementView, name='achievements'),
    path('Certification/<int:pk>', CertificationView, name='certifications'),
    path('Download/<int:pk>', DownloadView, name='download'),
    path('Resume/<int:pk>/', resumeView, name='resume'),
    path('works/', works, name='works'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
