from django.urls import path
from . import views
urlpatterns=[path('',views.home,name="name"),
            path('about',views.about,name="about"),
            path('skills',views.skill,name="skill"),
            path('dream',views.dream,name="dream"),
]