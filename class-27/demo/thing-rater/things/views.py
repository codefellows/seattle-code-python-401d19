from django.views.generic import ListView, DetailView
from .models import Thing


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing

    # if you add code below then templates can use things vs. object_list
    # context_object_name = "things"


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing
