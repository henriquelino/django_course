from async_timeout import Any
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json


class IndexView(TemplateView):
    template_name = 'index.html'


class RoomView(TemplateView):
    template_name = 'room.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['json_room_name'] = mark_safe(
            json.dumps(self.kwargs['room_name']))

        return context


def index(request):
    return render(request, 'chat/index.html')


# def room(request, room_name):
#     return render(request, 'chat/room.html', {'room_name_json': room_name})


def room(request, room_name):
    print('~~~DEBUG~~~')
    return render(request, 'room.html', {'room_name': room_name})
