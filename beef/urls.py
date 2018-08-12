from django.urls import path
from . import views


urlpatterns = [

    path('', views.beef, name="beef"),
    path('<int:beef_id>/', views.bigbeef, name='bigbeef'),
    
]
