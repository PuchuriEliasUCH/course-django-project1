from django.http import HttpResponse
import datetime

from django.shortcuts import render

def saludo(req):
  fecha_actual = datetime.datetime.now()

  context = {
    'name': 'Daniel', 
    'surname': 'Puchuri', 
    'today': fecha_actual, 
    'temas': [
      'Instalación', 
      'Plantillas', 
      'Modelos', 
      'Formularios',
      'Despliegue'  
      ],
    }
  
  return render(req, 'primeraPlantilla.html', context)

def despedida(req):
  return HttpResponse("Gracias por visitar mi sitio")

def fechaActual(req):
  fecha_actual = datetime.datetime.now()

  documento = f"""<html>
  <body>
  <h2>{fecha_actual}</h2>
  </body>
  </html>"""

  return HttpResponse(documento)

def calculaEdad(req, edad, anio):
  documento = f"""<html>
  <body>
  <h2>Tu edad será: {edad + anio - datetime.datetime.today().year}</h2>
  </body>
  </html>"""

  return HttpResponse(documento)

def herencia1_html(req):
  context = {} 
  return render(req, './herencia_templ/hijo1.html', context)

def herencia2_html(req):
  context = {} 
  return render(req, './herencia_templ/hijo2.html', context)