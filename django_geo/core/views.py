from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data


class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []
        context = {}
        city = None

        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']

        context['city'] = city
        context['user_search'] = False

        keyword = request.GET.get('keyword', None)
        location = request.GET.get('location', city)
        if location == "":
            location = city
        print(keyword, location, city)
        if keyword:
            items = yelp_search(keyword=keyword, location=location)
            print(items)
            context['items'] = items
            context['user_search'] = True

        return render(request, 'index.html', context)
