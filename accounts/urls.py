from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
]
