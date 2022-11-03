from django.urls import path
from .views import ReportLabView, WeasyprintView


urlpatterns = [
    path('1/', ReportLabView.as_view(), name='reportlab'),
    path('2/', WeasyprintView.as_view(), name='weasy'),
] # yapf: disable