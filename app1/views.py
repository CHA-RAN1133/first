from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse




def naveen(request):
    return HttpResponse('naveen can drink full bottel in single sitting without mixing thumpsup.')



def charan(request):
    return HttpResponse('<h1>charan drinks RS130 wine with ice-cubes and act as full kaipu</h1>')


def gani(request):
    return HttpResponse('gani cant drink in sitting without mixing thumpsup.')