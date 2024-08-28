from django.shortcuts import render


def main_home(request):
    return render(request, 'books/home.html')


def context(request):
    return render(request, 'books/conteckst.html')


def kontakt(request):
    return render(request, 'books/kontakt.html')
