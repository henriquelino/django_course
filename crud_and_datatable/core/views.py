from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Produto


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateUpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('index')


# create and update
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('index')
