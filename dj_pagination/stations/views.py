from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page = request.GET.get('page', 1)
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)#, fieldnames=('Name', 'Street', 'District')
        CONTENT= []
        reader_dict = {}
        for row in reader:
            reader_dict.update(row)
            CONTENT.append({'Name': str(reader_dict['Name']),
                            'Street':str(reader_dict['Street']),
                            'District':str(reader_dict['District'])})
    paginator_bus = Paginator(CONTENT, 10)
    bus_stations = paginator_bus.get_page(page)
    context = {
        'bus_stations': bus_stations,
    }
    return render(request, 'stations/index.html', context)
