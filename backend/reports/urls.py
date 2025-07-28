from django.urls import path
from .views import submit_accident_report

urlpatterns = [
    path('submit/', submit_accident_report, name='submit-accident'),
]
