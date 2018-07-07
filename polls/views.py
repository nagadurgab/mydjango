from django.http import HttpResponse


def index(request):
    return HttpResponse(" world. You're at the polls index.")