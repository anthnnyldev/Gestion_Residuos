from django.db import models

class WasteData(models.Model):
    region_id = models.CharField(max_length=10)
    country_name = models.CharField(max_length=255)
    gdp = models.FloatField()
    food_waste = models.FloatField()  # composition_food_organic_waste_percent
    glass_waste = models.FloatField()  # composition_glass_percent
    metal_waste = models.FloatField()  # composition_metal_percent
    other_waste = models.FloatField()  # composition_other_percent
    paper_waste = models.FloatField()  # composition_paper_cardboard_percent
    plastic_waste = models.FloatField()  # composition_plastic_percent
    rubber_waste = models.FloatField()  # composition_rubber_leather_percent
    wood_waste = models.FloatField()  # composition_wood_percent
    garden_waste = models.FloatField()  # composition_yard_garden_green_waste_percent

    # Special Waste Types
    agricultural_waste = models.FloatField()  # special_waste_agricultural_waste_tons_year
    construction_waste = models.FloatField()  # special_waste_construction_and_demolition_waste_tons_year
    ewaste = models.FloatField()  # special_waste_e_waste_tons_year
    hazardous_waste = models.FloatField()  # special_waste_hazardous_waste_tons_year
    industrial_waste = models.FloatField()  # special_waste_industrial_waste_tons_year
    medical_waste = models.FloatField()  # special_waste_medical_waste_tons_year

    # MSW Data
    total_msw = models.FloatField()  # total_msw_total_msw_generated_tons_year

    # Waste Collection Coverage
    waste_collection_urban_area_percent = models.FloatField()  # waste_collection_coverage_urban_percent_of_geographic_area
    waste_collection_urban_households_percent = models.FloatField()  # waste_collection_coverage_urban_percent_of_households
    waste_collection_urban_population_percent = models.FloatField()  # waste_collection_coverage_urban_percent_of_population
    waste_collection_urban_waste_percent = models.FloatField()  # waste_collection_coverage_urban_percent_of_waste

    # Waste Treatment
    anaerobic_digestion_percent = models.FloatField()  # waste_treatment_anaerobic_digestion_percent
    compost_percent = models.FloatField()  # waste_treatment_compost_percent
    controlled_landfill_percent = models.FloatField()  # waste_treatment_controlled_landfill_percent
    incineration_percent = models.FloatField()  # waste_treatment_incineration_percent
    recycling_percent = models.FloatField()  # waste_treatment_recycling_percent

    # Data source and legal information
    info_system = models.CharField(max_length=255)  # other_information_information_system_for_solid_waste_management
    national_agency = models.CharField(max_length=255)  # other_information_national_agency_to_enforce_solid_waste_laws_and_regulations
    national_law = models.CharField(max_length=255)  # other_information_national_law_governing_solid_waste_management_in_the_country
    public_info = models.TextField()  # other_information_summary_of_key_solid_waste_information_made_available_to_the_public

    # Population and waste data
    population = models.IntegerField()  # population_population_number_of_people
    waste_collection_coverage_total_percent = models.FloatField()  # waste_collection_coverage_total_percent_of_geographic_area

    def __str__(self):
        return self.country_name
