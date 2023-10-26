from django.shortcuts import render

from .search import lookup


def search_view(request):

    q = request.GET.get('q')

    context = {}

    if q is not None:
        results = lookup(q)
        context['results'] = results
        context['query'] = q

    return render(request, 'search.html', context)
