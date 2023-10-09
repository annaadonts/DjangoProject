from django.urls import path
from .views import index, run_script

urlpatterns = [
    path('', index, name='index'),
    path('run_script/', run_script, name='run_script'),
]
