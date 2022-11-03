from django.urls import path

from .views import IndexView, JSONDataView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('data/', JSONDataView.as_view(), name='data')
]