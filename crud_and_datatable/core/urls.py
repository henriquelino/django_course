from django.urls import path
from .views import IndexView, CreateProdutoView, UpdateProdutoView, CreateUpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('create/', CreateProdutoView.as_view(), name='create_produto'),
    # path('update/<int:pk>', UpdateProdutoView.as_view(),
    #      name='update_produto'),
    path('create/', CreateUpdateProdutoView.as_view(), name='create_produto'),
    path('update/<int:pk>',
         CreateUpdateProdutoView.as_view(),
         name='update_produto'),
    path('delete/<int:pk>', DeleteProdutoView.as_view(), name='delete_produto')
]
