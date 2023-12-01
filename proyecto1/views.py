from django.http import HttpResponse
import datetime

def saludo(req):  
  return HttpResponse("Bienvenidos al framework Django")

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