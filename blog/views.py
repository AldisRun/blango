from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "blog/index.html")

# Create your views here.
