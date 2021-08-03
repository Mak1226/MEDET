"""medet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users.views import MedicineDetailView,MedicineCreateView,MedicineUpdateView,MedicineDeleteView
from users.views import DoctorDetailView,DoctorCreateView,DoctorUpdateView,DoctorDeleteView,ScheduleDetailView
from users.views import DiseaseDetailView,DiseaseCreateView,DiseaseUpdateView,DiseaseDeleteView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),
    path('register/',user_views.register,name="register"),
    path('profile/',user_views.profile,name="profile"),
    path('profile/medicine/',user_views.medicine,name="profile_medicine"),
    path('profile/disease/',user_views.disease,name="profile_disease"),
    path('profile/doctor/',user_views.doctor,name="profile_doctor"),
    path('profile/schedule/',user_views.schedule,name="profile_schedule"),

    path('profile/doctor/<int:pk>/',DoctorDetailView.as_view(),name="profile_doc_detail"),
    path('profile/doctor/new/',DoctorCreateView.as_view(),name="profile_doc_create"),
    path('profile/doctor/<int:pk>/update/',DoctorUpdateView.as_view(),name="profile_doc_update"),
    path('profile/doctor/<int:pk>/delete/',DoctorDeleteView.as_view(),name="profile_doc_delete"),

    path('profile/schedule/<int:pk>/',ScheduleDetailView.as_view(),name="profile_schedule_detail"),

    path('profile/disease/<int:pk>/',DiseaseDetailView.as_view(),name="profile_disease_detail"),
    path('profile/disease/new/',DiseaseCreateView.as_view(),name="profile_disease_create"),
    path('profile/disease/<int:pk>/update/',DiseaseUpdateView.as_view(),name="profile_disease_update"),
    path('profile/disease/<int:pk>/delete/',DiseaseDeleteView.as_view(),name="profile_disease_delete"),



    path('profile/medicine/<int:pk>/',MedicineDetailView.as_view(),name="profile_med_detail"),
    path('profile/medicine/new/',MedicineCreateView.as_view(),name="profile_med_create"),
    path('profile/medicine/<int:pk>/update/',MedicineUpdateView.as_view(),name="profile_med_update"),
    path('profile/medicine/<int:pk>/delete/',MedicineDeleteView.as_view(),name="profile_med_delete"),

    path('profile_update/',user_views.profile_update,name="profile_update"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout')
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
