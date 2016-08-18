
from io import BytesIO


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm

from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
	return HttpResponse("Hola mundo Django!!!!")

def	report(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachement; filename=Anthony Carrillo Rosales'

	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize = A4)

	c.setLineWidth(.3)
	c.drawString(30,70,'Lo logre!!!!!')

	c.save()

	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response