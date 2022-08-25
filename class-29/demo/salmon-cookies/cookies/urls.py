from django.urls import path
from .views import CookieStandListView

urlpatterns = [
    path("", CookieStandListView.as_view(), name="cookie_stand_list"),
]
