from django.http import HttpResponse

def saludo(req):  
  return HttpResponse("Bienvenidos al framework Django")

def despedida(req):
  return HttpResponse("Gracias por visitar mi sitio")