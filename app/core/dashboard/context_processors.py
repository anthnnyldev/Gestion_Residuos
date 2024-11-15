from django.db import models
from core.dashboard.models import Points

def total_points(request):
    if request.user.is_authenticated:
        # Calcula los puntos directamente desde el modelo Points
        total_points = Points.objects.filter(user=request.user).aggregate(total=models.Sum('number'))['total'] or 0
    else:
        total_points = 0

    return {'total_points': total_points}
