from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.contrib import messages
from core.dashboard.models import ProductRequest, Points, PointHistory

class ProductRequestListView(ListView):
    model = ProductRequest
    template_name = "core/points/product_requests.html"
    context_object_name = "requests"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ProductRequest.objects.all().order_by('-created_at')
        else:
            return ProductRequest.objects.filter(user=user).order_by('-created_at')


class ProductRequestActionView(View):
    def post(self, request, pk):
        product_request = get_object_or_404(ProductRequest, pk=pk)
        action = request.POST.get("action")
        points = int(request.POST.get("points", 0))

        if not request.user.is_superuser:
            messages.error(request, "No tienes permiso para realizar esta acción.")
            return redirect("dashboard:product_requests_list")

        if action == "approve":
            if points < 0:
                messages.error(request, "No se pueden asignar puntos negativos.")
                return redirect("dashboard:product_requests_list")

            product_request.approve(admin_user=request.user, points=points)
            
            points_record = Points.objects.create(
                user=product_request.user,
                number=points,
                action_type='PRODUCT_REQUEST',
                created_by=request.user
            )

            PointHistory.objects.create(
                user=product_request.user,
                points=points,
                action=f"Aprobación de solicitud para {product_request.product.name}",
                created_by=request.user
            )

            messages.success(request, "La solicitud fue aprobada y los puntos asignados correctamente.")
        elif action == "deny":
            product_request.deny(admin_user=request.user)
            messages.success(request, "La solicitud fue denegada.")
        else:
            messages.error(request, "Acción inválida.")

        return redirect("dashboard:product_requests_list")
    
class PointHistoryListView(ListView):
    model = PointHistory
    template_name = "core/points/point_history.html"
    context_object_name = "point_histories"

    def get_queryset(self):
        return PointHistory.objects.filter(user=self.request.user).order_by('-created_at')
