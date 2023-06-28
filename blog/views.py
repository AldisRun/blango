from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def helloworld(request):
    logging.error('Hello world Blog in the log...')
    print('Hello world Blog in a print statement...')
    response = """<html><body><p>Hello world Blog in HTML</p>
    <p>This sample code is available at
    </p>
    </body></html>"""
    return HttpResponse(response)

# Create your views here.
