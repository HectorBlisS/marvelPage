from django.shortcuts import render
from django.views.generic import View
from .mv import Marvel


class Home(View):
	def get(self,request):
		template_name = 'marvel/home.html'
		return render(request,template_name)

	def post(self,request):
		heroe = request.POST.get('heroe')
		mv = Marvel()
		personaje = mv.get_personaje(heroe)
		link = mv.get_imagen()
		template_name = 'marvel/home.html'
		context = {
		'personaje':personaje,
		'heroe':heroe,
		'link':link
		}
		return render(request,template_name,context)
