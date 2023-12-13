from django.urls import path,include
from deseri import views

urlpatterns = [
    path('stucreate/',views.stucreate,name='stucreate')
]
