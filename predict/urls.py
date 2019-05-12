from django.urls import path
from . import views

app_name = 'predict'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    path('predict/', views.predict, name='predict'),
]
