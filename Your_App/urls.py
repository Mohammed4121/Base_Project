from django.urls import path

from Your_App.views import home



urlpatterns = [
    path('', view=home, name='home'),
]
