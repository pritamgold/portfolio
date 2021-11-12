from django.shortcuts import render

# Create your views here.
def services(request):
    context = {'contact': 'active'}
    return render(request, 'serv/services.html')
