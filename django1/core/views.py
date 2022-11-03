from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Produto


# Create your views here.
def index(request: WSGIRequest):
    produtos = Produto.objects.all()
    context = {
        "curso": "Programação web com django",
        "outro": "Django é massa",
        "produtos": produtos
    }
    return render(request, "index.html", context)


def produto(request: WSGIRequest, pk):
    print(type(request))

    prod = get_object_or_404(Produto, id=pk)

    context = {
        "curso": "Programação web com django",
        "outro": "Django é massa",
        "produto": prod
    }

    return render(request, "produto.html", context)


def contato(request: WSGIRequest):
    return render(request, "contato.html")


def error404(request: WSGIRequest, exception):
    template = loader.get_template("404.html")
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404)


def error500(request: WSGIRequest):
    template = loader.get_template("500.html")
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500)
