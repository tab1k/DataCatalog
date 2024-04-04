from django.shortcuts import render
from django.views.generic import TemplateView


class InformationView(TemplateView):
    template_name = 'main/information.html'

    def get_context_data(self, **kwargs):
        pass