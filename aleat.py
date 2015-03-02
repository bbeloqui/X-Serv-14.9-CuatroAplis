#!/usr/bin/python
import random
import webapp

class aleat:

	def parse(self, request, reset):  #no haria falta ponerlo
		return None

	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>Pagina aleatoria</h1>" + "<a href='/aleat/"+
				str(random.randrange(999999)) + "'>Dame otra</a>" + "</body></html>")
