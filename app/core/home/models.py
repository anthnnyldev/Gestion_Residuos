from django.db import models

class WasteComposition(models.Model):
    region_id = models.IntegerField()
    country_name = models.CharField(max_length=100)
    gdp = models.DecimalField(max_digits=15, decimal_places=2)
    composition_food_organic_waste_percent = models.FloatField()
    composition_glass_percent = models.FloatField()
    composition_metal_percent = models.FloatField()
    composition_other_percent = models.FloatField()
    composition_paper_cardboard_percent = models.FloatField()
    composition_plastic_percent = models.FloatField()
    composition_rubber_leather_percent = models.FloatField()

    def __str__(self):
        return self.country_name
