from math import ceil

from django.shortcuts import render

from apps.models import Card


def index_view(request):
    cards = Card.objects.order_by('-posted_at')
    page = int(request.GET.get('page', 1))
    last_page_number = -1
    if page:
        page_size = 6
        cards = cards[page_size * (page - 1):page_size * page]
        last_page_number = ceil(Card.objects.count() / page_size)
    context = {
        'cards': cards,
        'last_page_number': last_page_number,
    }
    return render(request, 'apps/index.html', context)
