from django.urls import path 

from .views import home


app_name = "multapp"
urlpatterns = [
    path("", home, name="home")
]
