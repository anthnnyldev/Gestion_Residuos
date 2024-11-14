import csv
import json
from django.shortcuts import render
from django.conf import settings
import os

def load_waste_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'home', 'data', 'data.csv')

    countries = []
    food_waste = []
    plastic_waste = []
    paper_waste = []
    metal_waste = []

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            countries.append(row['country_name'])  # Nombre del país
            
            # Función para convertir valores a float, manejando 'NA'
            def safe_float(value):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return 0.0  # Puedes elegir un valor por defecto o manejarlo de otra manera
            
            food_waste.append(safe_float(row['composition_food_organic_waste_percent']))  # % de residuos orgánicos
            plastic_waste.append(safe_float(row['composition_plastic_percent']))  # % de plásticos
            paper_waste.append(safe_float(row['composition_paper_cardboard_percent']))  # % de papel
            metal_waste.append(safe_float(row['composition_metal_percent']))  # % de metales

    # Convert data to JSON before passing to the template
    data_json = json.dumps({
        'countries': countries,
        'food_waste': food_waste,
        'plastic_waste': plastic_waste,
        'paper_waste': paper_waste,
        'metal_waste': metal_waste
    })

    return render(request, 'home/ecovision.html', {'data': data_json})