from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    data = {"nombre": "Ignacio", "apellido": "Aguirre", "edad": "23"}

    return render(request, 'appInventario/primerTemplate.html', data)