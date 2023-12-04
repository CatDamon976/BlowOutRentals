from django.shortcuts import render
from django.http import HttpResponse


def indexPageView(request) :
     return render(request, 'homepages/index.html')

def aboutPageView(request) :
     return render(request, 'homepages/about.html')

def instrumentPageView(request) :
     return render(request, 'inventory/instrument.html')



def trumpet_detail_view(request, instrument_name, instrument_id):
    return render(request, 'inventory/trumpet.html', {'name': instrument_name, 'id': instrument_id})
