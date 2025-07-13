from django.urls import path
from .views import vastu_analysis_view

urlpatterns = [
    path('api/analyze/', vastu_analysis_view),
]
