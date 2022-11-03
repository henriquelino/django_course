import json

from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


# Create your views here.
def index(request: WSGIRequest):
    context = {"produtos": Produto.objects.all()}
    return render(request, 'index.html', context)


def contato(request: WSGIRequest):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # print(f"formulário recebido:\n{json.dumps(form.cleaned_data, indent=4)}")
            form.send_mail()
            messages.success(request, "E-mail enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, "Falha ao enviar e-mail")
    else:
        form = ContatoForm()

    context = {"form": form}
    return render(request, 'contato.html', context)


def produto(request: WSGIRequest):
    if str(request.user) == 'AnonymousUser':
        return redirect("/admin")

    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            # print(f"Produto recebido:\n{json.dumps(produto.__dict__, indent=4, default=str)}")
            form.save()
            messages.success(request, "Produto cadastrado com sucesso")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Falha ao cadastrar produto")
    else:
        form = ProdutoModelForm()

    context = {"form": form}
    return render(request, 'produto.html', context)
