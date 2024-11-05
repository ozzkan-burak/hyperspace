from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Wecome to Hyperspace, this message with Core")

