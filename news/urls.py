from django.urls import path
from news import views

urlpatterns = [
    path('', views.shownews, name='shownews'),
    path('business/', views.shownews1, name='shownews1'),
    path('indin/', views.shownews2, name='shownews2'),
    path('sports/', views.shownews3, name='shownews3'),
    path('world/', views.shownews4, name='shownews4'),
    path('politics/', views.shownews5, name='shownews5'),
    path('entertainment/', views.shownews6, name='shownews6'),
    path('miscellaneous/', views.shownews7, name='shownews7'),
    path('startup/', views.shownews8, name='shownews8'),
    path('technology/', views.shownews9, name='shownews9'),
    path('hindi/', views.shownewshindi0, name='shownewshindi0'),
    path('hindi/business/', views.shownewshindi1, name='shownews1hindi'),
    path('hindi/indin/', views.shownewshindi2, name='shownewshindi2'),
    path('hindi/sports/', views.shownewshindi3, name='shownewshindi3'),
    path('hindi/world/', views.shownewshindi4, name='shownewshindi4'),
    path('hindi/politics/', views.shownewshindi5, name='shownewshindi5'),
    path('hindi/entertainment/', views.shownewshindi6, name='shownewshindi6'),
    path('hindi/miscellaneous/', views.shownewshindi7, name='shownewshindi7'),
    path('hindi/startup/', views.shownewshindi8, name='shownewshindi8'),
    path('hindi/technology/', views.shownewshindi9, name='shownewshindi9'),
]