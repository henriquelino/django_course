from typing import Any

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.generic import FormView, TemplateView

from .forms import ContactForm
from .models import Feature, Service, TeamMember


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Retrieve additional data for index.html before page load"""
        context = super().get_context_data(**kwargs)

        context['language'] = translation.get_language()
        context['services'] = Service.objects.order_by('?').all()
        context['team'] = TeamMember.objects.order_by('?').all()
        context['features'] = Feature.objects.order_by('?').all()
        translation.activate(context['language'])
        return context

    def form_valid(self, form: ContactForm, *args, **kwargs) -> HttpResponse:
        """If contact form is valid, send an email"""
        form.send_email()
        messages.success(self.request, _('E-mail enviado com sucesso!'))  # _ to translate these texts
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form: ContactForm, *args, **kwargs) -> HttpResponse:
        """If contact form is invalid"""
        messages.error(self.request, _('Erro ao enviar e-mail'))  # _ to translate these texts
        return super().form_invalid(form, *args, **kwargs)


class TesteView(TemplateView):
    template_name = '500.html'
