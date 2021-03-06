from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class StartPageView(TemplateView):
    template_name = "start_page.html"


class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
	template_name = "about.html"
