import csv
from django.shortcuts import render
from django.conf import settings
import os

def load_waste_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'home', 'data', 'data.csv')

    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    return render(request, 'home/ecovision.html', {'data': data})
