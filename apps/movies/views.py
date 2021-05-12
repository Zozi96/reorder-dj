from django.db import transaction
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from apps.movies.form import OrderingForm
from apps.movies.models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/table.html'


@require_POST
def save_ordering(request):
    form = OrderingForm(request.POST)

    if form.is_valid():
        ordered_ids = form.cleaned_data["ordering"].split(',')

        with transaction.atomic():
            current_order = 1
            for lookup_id in ordered_ids:
                movie = Movie.objects.get(lookup_id__exact=lookup_id)
                movie.order = current_order
                movie.save()
                current_order += 1
    return redirect('list')
