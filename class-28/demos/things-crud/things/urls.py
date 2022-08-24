from django.urls import path
from .views import ThingListView, ThingDetailView, ThingCreateView, ThingUpdateView, ThingDeleteView

urlpatterns = [
    path("list/", ThingListView.as_view(), name="thing_list"),
    path("detail/<int:pk>/", ThingDetailView.as_view(), name="thing_detail"),
    path("create/", ThingCreateView.as_view(), name="thing_create"),
    path("update/<int:pk>/", ThingUpdateView.as_view(), name="thing_update"),
    path("delete/<int:pk>/", ThingDeleteView.as_view(), name="thing_delete"),
]
