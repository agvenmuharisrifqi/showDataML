from django.shortcuts import render

def index(request):
    context = {
        'title': 'SHOW DATA ML'
    }
    return render(request, 'index.html', context)