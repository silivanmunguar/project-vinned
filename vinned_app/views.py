from django.shortcuts import render
from django.http import HttpResponse
from . import api_requests


# Create your views here.
# def home_page(request):
#     vin="4F2YU09161KM33122"
#     info = api_requests.getVinInfo(vin)
#     return render(request, 'index.html', info)


def home_page(request):
    return render(request, 'index.html')

def vin_info(request):
    if request.method == 'POST':
        vin = request.POST['vin#']
        info = api_requests.getVinInfo(vin)
        return render(request, 'results.html', info)
        