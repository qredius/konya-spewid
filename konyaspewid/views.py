from django.shortcuts import render
from django.template import RequestContext

def index(request):
	context = {}
	templates = 'index.html'
	return render(request, templates, context)
def services(request):
	context = {}
	templates = 'services.html'
	return render(request, templates, context)

def aboutus(request):
	context = {}
	templates = 'aboutus.html'
	return render(request, templates, context)

def contact(request):
	context = {}
	templates = 'contact.html'
	return render(request, templates, context)

def vacancies(request):
	context = {}
	templates = 'vacancies.html'
	return render(request, templates, context)

def portfolio(request):
	context = {}
	templates = 'portfolio.html'
	return render(request, templates, context)

def aboutevr(request):
	context = {}
	templates = 'aboutevr.html'
	return render(request, templates, context)

def abouthaw(request):
	context = {}
	templates = 'abouthaw.html'
	return render(request, templates, context)

def abouthr(request):
	context = {}
	templates = 'abouthr.html'
	return render(request, templates, context)