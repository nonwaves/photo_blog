from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'


class LogOutPage(TemplateView):
    template_name = 'loggedout.html'