import csv
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from core.home.models import WasteComposition

class UploadCSVView(View):
    template_name = 'home/ecovision.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.FILES.get('file'):
            file = request.FILES['file']
            file_data = file.read().decode("utf-8")
            lines = file_data.splitlines()
            reader = csv.DictReader(lines)

            WasteComposition.objects.all().delete()
            for row in reader:
                WasteComposition.objects.create(
                    region_id=int(row['region_id']),
                    country_name=row['country_name'],
                    gdp=float(row['gdp']),
                    composition_food_organic_waste_percent=float(row['composition_food_organic_waste_percent']),
                    composition_glass_percent=float(row['composition_glass_percent']),
                    composition_metal_percent=float(row['composition_metal_percent']),
                    composition_other_percent=float(row['composition_other_percent']),
                    composition_paper_cardboard_percent=float(row['composition_paper_cardboard_percent']),
                    composition_plastic_percent=float(row['composition_plastic_percent']),
                    composition_rubber_leather_percent=float(row['composition_rubber_leather_percent']),
                )
            messages.success(request, "CSV subido y datos guardados exitosamente")
            return redirect('datos_html')
        return render(request, self.template_name)
