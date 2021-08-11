from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('exams_api/fonte/<int:pk>/', views.FonteUpdate.as_view(), name='fonte-update'),
    url(r'^exams_api/fonte/$', views.FonteList.as_view(), name='fonte-list'),

    path('exams_api/assunto/<int:pk>/', views.AssuntoUpdate.as_view(), name='assunto-update'),
    url(r'^exams_api/assunto/$', views.AssuntoList.as_view(), name='assunto-list'),

    url(r'^exams_api/tipoassunto/$', views.TipoAssuntoList.as_view(), name='tipoassunto-list'),

    path('exams_api/questao/<int:pk>/', views.QuestaoUpdate.as_view(), name='questao-update'),
    path('exams_api/questao/', views.QuestaoList.as_view(), name='questao-list'),

    path('exams_api/alternativas/<int:pk>/', views.AlternativasUpdate.as_view(), name='alternativas-update'),
    url(r'^exams_api/alternativas/$', views.AlternativasList.as_view(), name='alternativas-list'),
]


    # url(r'^exams_api/questao/<pk>$', views.UpdateQuestao.as_view(), name='questao-update'),