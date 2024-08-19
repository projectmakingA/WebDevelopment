from django.urls import path,include
from . import views

urlpatterns=[
    path('student/',views.student_register,name='student_register'),
    path('',views.base,name='base'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('teacher/',views.teacher_register,name='teacher_register'),
]