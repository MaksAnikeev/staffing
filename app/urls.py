from django.urls import path

from .views import index_page

app_name = "app"

urlpatterns = [
    path('', index_page, name="index_page"),
]