from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Hola(View):
	def get(self,request):
		return HttpResponse("Hey! entraste a mi sitio! t(O_Ot)")
