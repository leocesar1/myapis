from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('exams_api/source/<int:pk>/', views.SourceUpdate.as_view(), name='source-update'),
    url(r'^exams_api/source/$', views.SourceList.as_view(), name='source-list'),

    path('exams_api/topic/<int:pk>/', views.TopicUpdate.as_view(), name='topic-update'),
    url(r'^exams_api/topic/$', views.TopicList.as_view(), name='topic-list'),

    path('exams_api/question/<int:pk>/', views.QuestionUpdate.as_view(), name='question-update'),
    path('exams_api/question/', views.QuestionList.as_view(), name='question-list'),

    path('exams_api/alternatives/<int:pk>/', views.AlternativesUpdate.as_view(), name='alternatives-update'),
    url(r'^exams_api/alternatives/$', views.AlternativesList.as_view(), name='alternatives-list'),
]


    # url(r'^exams_api/questao/<pk>$', views.UpdateQuestao.as_view(), name='questao-update'),