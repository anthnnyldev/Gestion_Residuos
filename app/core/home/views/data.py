import os
import csv
import json
from django.shortcuts import render
from django.conf import settings

# Function to safely convert a value to float
def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def load_waste_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'home', 'data', 'data.csv')

    waste_data = {}
    year_data = {}  # For the trend chart, you could aggregate by year
    for waste_type in ['food_waste', 'plastic_waste', 'paper_waste', 'metal_waste']:
        year_data[waste_type] = {}

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            country_name = row['country_name']
            # Fill data for waste composition
            waste_data[country_name] = {
                'food_waste': safe_float(row['composition_food_organic_waste_percent']),
                'plastic_waste': safe_float(row['composition_plastic_percent']),
                'paper_waste': safe_float(row['composition_paper_cardboard_percent']),
                'metal_waste': safe_float(row['composition_metal_percent']),
            }

            # Sample data for trends
            year = row.get('year', '2020')  # Assumed column for years in data.csv
            for waste_type in ['food_waste', 'plastic_waste']:
                if year not in year_data[waste_type]:
                    year_data[waste_type][year] = 0
                year_data[waste_type][year] += waste_data[country_name].get(waste_type, 0)

    return render(request, 'home/ecovision.html', {
        'data': json.dumps(waste_data),
        'year_data': json.dumps(year_data),
    })


def country_detail(request, country_name):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'home', 'data', 'data.csv')
    country_data = {}

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['country_name'].lower() == country_name.lower():
                country_data = {
                    'country_name': row['country_name'],
                    'food_waste': safe_float(row['composition_food_organic_waste_percent']),
                    'plastic_waste': safe_float(row['composition_plastic_percent']),
                    'paper_waste': safe_float(row['composition_paper_cardboard_percent']),
                    'metal_waste': safe_float(row['composition_metal_percent']),
                    'waste_treatment_recycling': safe_float(row['waste_treatment_recycling_percent']),
                    'waste_treatment_incineration': safe_float(row['waste_treatment_incineration_percent']),
                    'waste_treatment_landfill': safe_float(row['waste_treatment_controlled_landfill_percent']),
                    'waste_collection_rural': safe_float(row['waste_collection_coverage_rural_percent_of_population']),
                    'waste_collection_urban': safe_float(row['waste_collection_coverage_urban_percent_of_population']),
                    'special_waste_electronic': safe_float(row['special_waste_e_waste_tons_year']),
                    'special_waste_industrial': safe_float(row['special_waste_industrial_waste_tons_year']),
                    'special_waste_medical': safe_float(row['special_waste_medical_waste_tons_year']),
                    # Agrega más campos si es necesario
                }
                break

    return render(request, 'home/country_detail.html', {
        'country_data': json.dumps(country_data)
    })
