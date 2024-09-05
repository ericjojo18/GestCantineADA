from django.urls import path
from cantine.views.plat_views import index, add_plat, update_plat, delete_plat

app_name = "plat"

urlpatterns = [
    path("", index, name="index"),
    path("add_plat/", add_plat, name="add_plat"),
    path("update_plat/<int:id>/", update_plat, name="update_plat"),
    path("delete_plat/<int:id>/", delete_plat, name="delete_plat"),
]