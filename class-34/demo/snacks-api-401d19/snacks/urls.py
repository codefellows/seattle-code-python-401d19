from django.urls import path
from .views import SnackList, SnackDetail

urlpatterns = [
    path("", SnackList.as_view(), name="thing_list"),
    path("<int:pk>/", SnackDetail.as_view(), name="thing_detail"),
]
