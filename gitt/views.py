
from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'gitt/home.html')


def Porcelain(request):
    return render(request, 'gitt/porcelain.html')


def Ancillary(request):
    return render(request, 'gitt/ancillary.html')


def Interaction(request):
    return render(request, 'gitt/interaction.html')


def Manipulation(request):
    return render(request, 'gitt/manipulation.html')


def Interrogation(request):
    return render(request, 'gitt/interrogation.html')


def Syncing(request):
    return render(request, 'gitt/syncing.html')


def Helper(request):
    return render(request, 'gitt/helper.html')


def Mistakes(request):
    return render(request, 'gitt/mistakes.html')
