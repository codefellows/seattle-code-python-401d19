from django.urls import path
from .views import StandListView

urlpatterns = [
    path("", StandListView.as_view(), name="stand_list"),
]
