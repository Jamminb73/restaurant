from django.urls import path
from . import views


urlpatterns = [

    path('', views.pork, name="pork"),
    path('<int:pork_id>/', views.bigpork, name='bigpork'),
]
