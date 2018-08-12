from django.urls import path
from . import views


urlpatterns = [

    path('', views.chicken, name="chicken"),
    path('<int:chicken_id>/', views.bigchicken, name='bigchicken'),
    ]
