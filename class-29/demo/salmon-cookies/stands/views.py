from django.views.generic import ListView
from .models import Stand


class StandListView(ListView):
    template_name = "stand_list.html"
    model = Stand
    context_object_name = "stands"

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["labels"] = ["7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm",
                             "7pm", "Total"]

        cross_store_hourly_totals = []
        mega_tally = 0

        for hourly_index in range(13):
            tally = 0
            for stand in self.object_list:
                tally += stand.sales[hourly_index]
            cross_store_hourly_totals.append(tally)
            mega_tally += tally

        cross_store_hourly_totals.append(mega_tally)

        context["cross_store_hourly_totals"] = cross_store_hourly_totals

        return context
