from django.db import models
from core.dashboard.models import Points, PointHistory

def total_points(request):
    if request.user.is_authenticated:
        total_points = Points.objects.filter(user=request.user).aggregate(total=models.Sum('number'))['total'] or 0
        total_history_points = PointHistory.objects.filter(user=request.user).aggregate(total=models.Sum('points'))['total'] or 0
        total_points += total_history_points
        
    else:
        total_points = 0
        
    return {'total_points': total_points}
