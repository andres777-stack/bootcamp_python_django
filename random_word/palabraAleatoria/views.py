from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def aleatoria(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
        palAl = get_random_string(length = 14)
    else:
        request.session['counter'] = 1
        palAl = get_random_string(length = 14)
    context = {'contador': request.session['counter'], 'palabraAl': palAl}
    return render(request, 'index.html', context)
# Create your views here.
def index(request):
    return render(request, 'index.html')