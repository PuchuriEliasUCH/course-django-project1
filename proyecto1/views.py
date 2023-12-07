from django.http import HttpResponse
import datetime

from django.template import loader

def saludo(req):
  fecha_actual = datetime.datetime.now()
  # Comienza la busqueda en la raiz del proyecto
  doc_externo = loader.get_template('primeraPlantilla.html')

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
  documento = doc_externo.render(context)
  
  return HttpResponse(documento)

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