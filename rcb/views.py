from django.shortcuts import render

# Create your views here.
def conditions(request):
     d={'a':18,'b':210,'c':209}
     return render(request,'conditions.html',d)


def loop(request):
    d={'name':'somu'}
    return render(request,'loop.html',d)