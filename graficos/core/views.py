from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class JSONDataView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para o eixo X"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets"""
        datasets = [
            "Dataset 1",
            "Dataset 2",
            "Dataset 3",
            "Dataset 4",
            "Dataset 5",
            "Dataset 6",
        ]
        return datasets

    def get_data(self):
        """Retorna 6 datasets para plotar o grafico
        Cada linha representa um dataset.
        Cada coluna representa um label

        Quantidade de dados = datasets/labels
        12 labels = 12 colunas
        6 datasets = 6 linhas
        """
        dados = []

        for linha in range(6):  # para cada dataset
            for coluna in range(12):  # para cada label
                dado = [
                    # um para cada mes do ano
                    randint(1, 200),  # Janeiro
                    randint(1, 200),  # Fevereiro
                    randint(1, 200),  # Março
                    randint(1, 200),  # Abril
                    randint(1, 200),  # Maio
                    randint(1, 200),  # Junho
                    randint(1, 200),  # Julho
                    randint(1, 200),  # Agosto
                    randint(1, 200),  # Setembro
                    randint(1, 200),  # Outubro
                    randint(1, 200),  # Novembro
                    randint(1, 200),  # Dezembro
                ]
            dados.append(dado)

        return dados
