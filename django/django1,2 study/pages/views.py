from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': '도경원',
    }
    return render(request, 'pages/index.html', context)