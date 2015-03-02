#!/usr/bin/python
import webapp
class suma:
	def parse(self, request, rest):
		try:
			digito1 = int(rest.split("/")[1])
			digito2 = int(rest.split("/")[2])
		except ValueError:
			return None
		return (digito1, digito2)

	def process(self, parsedRequest):
		if not parsedRequest:
			return("400 Bad Request", "<html>" +
					"<body><h1>Error</h1>" +
					"</body></html>")

		solucion = (str(parsedRequest[0]) + " + " +
					str(parsedRequest[1]) + " = " +
					str(parsedRequest[0] + parsedRequest[1]))

		return("200 OK", "<html>" 
				+"<body><h1>" + solucion + "</h1></body></html>")
