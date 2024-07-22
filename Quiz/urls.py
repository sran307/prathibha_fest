from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('quiz_master',views.quizMaster, name='quiz_master'),
    path('class_list',views.classList, name='classList'),
    path('save_classlist', views.saveClasslist, name='save_classlist'),
    path('saveQuizton', views.saveQuizton, name="save_quizton"),
    path('quiztonList', views.quiztonList, name="quizton_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
