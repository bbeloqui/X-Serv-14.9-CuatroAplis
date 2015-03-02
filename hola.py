#!/usr/bin/python
import webapp

class hola:

	def parse(self, request, reset):  #no haria falta ponerlo
		return None

	def process(self, parsedRequest):
		return("200 Ok" ,"<html><body><h1>HOLA</h1></body></html>")


class adios:
 
	def parse(self, request, reset):  #no haria falta ponerlo
		return None

	def process(self, parseRequest):
		return("200 Ok" ,"<html><body><h1>ADIOS</h1></body></html>")

	
