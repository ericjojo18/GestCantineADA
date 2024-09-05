from django.urls import path, include

urlpatterns = [
    path("", include("cantine.Urls.menu_urls")),
    path("plat/", include("cantine.Urls.plat_urls")),
]