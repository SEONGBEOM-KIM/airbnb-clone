from django.urls import path
from rooms import views as room_Views

app_name = "core"

urlpatterns = [path("", room_Views.HomeView.as_view(), name="home")]
