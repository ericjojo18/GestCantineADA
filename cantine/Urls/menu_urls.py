from django.urls import path
from cantine.views.menus_views import home, index

app_name = "menus"

urlpatterns = [
    path("", home, name="home"),
    path("menus/", index, name="index"),
]