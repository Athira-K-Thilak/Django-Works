"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from operation.views import AdditionView,SubtractionView,MultiplicationView,DivisionView
from operation.views import SignUpView
from operation.views import VehicleAddView
from operation.views import BmrView
from operation.views import AppointmentView
from operation.views import BmiView
from operation.views import MilageView
from operation.views import CalorieView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/',AdditionView.as_view()),
    path('subtract/',SubtractionView.as_view()),
    path('multiply/',MultiplicationView.as_view()),
    path('division/',DivisionView.as_view()),
    path('register/',SignUpView.as_view()),
    path('vehicle/',VehicleAddView.as_view()),
    path('bmr/',BmrView.as_view()),
    path('appointment/',AppointmentView.as_view()),
    path('bmi/',BmiView.as_view()),
    path("milage/",MilageView.as_view()),
    path('calorie/',CalorieView.as_view(),)

]


