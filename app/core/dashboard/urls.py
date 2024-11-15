from django.urls import path
from core.dashboard.views import home, category, units, product, point

app_name = "dashboard"

urlpatterns = [
    #DASHBOARD
    path('',home.DashboardView.as_view(),name="home"),
    path('ver-productos/', home.ProductView.as_view(), name='product_view'),

    #CATEGORY
    path('categories/', category.CategoryListView.as_view(), name="category_list"),
    path('categories/create/', category.CategoryCreateView.as_view(), name="category_create"),
    path('categories/<int:pk>/update/', category.CategoryUpdateView.as_view(), name="category_update"),
    path('categories/<int:pk>/delete/', category.CategoryDeleteView.as_view(), name="category_delete"),

    #UNITS
    path('units/', units.UnitsListView.as_view(), name='unit_list'),
    path('units/create/', units.UnitsCreateView.as_view(), name='unit_create'),
    path('units/<int:pk>/edit/', units.UnitsUpdateView.as_view(), name='unit_edit'),
    path('units/<int:pk>/delete/', units.UnitsDeleteView.as_view(), name='unit_delete'),

    #PRODUCTS
    path('products/', product.ProductListView.as_view(), name='product_list'),
    path('products/create/', product.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', product.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', product.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/toggle-status/', product.ProductToggleStatusView.as_view(), name='product_toggle_status'),
    path('product/request/<int:product_id>/', home.ProductRequestCreateView.as_view(), name='request_product'),


    #REQUEST PRODUCT
    path('product-requests/', point.ProductRequestListView.as_view(), name='product_requests_list'),
    path('product-requests/action/<int:pk>/', point.ProductRequestActionView.as_view(), name='product_request_action'),

    #HISTORY POINT
    path('point-history/', point.PointHistoryListView.as_view(), name='point_history'),

    #REWARS
    path('rewards/', home.RewardListView.as_view(), name='rewards_list'),
    path('rewards/create/', home.RewardCreateView.as_view(), name='reward_create'),
    path('rewards/<int:pk>/edit/', home.RewardUpdateView.as_view(), name='reward_edit'),
    path('rewards/<int:pk>/delete/', home.RewardDeleteView.as_view(), name='reward_delete'),

    path("redeem/<int:pk>/confirm/", home.RedeemRewardConfirmationView.as_view(), name="redeem_confirm"),
    path("redeem/<int:pk>/", home.RedeemRewardView.as_view(), name="redeem"),
]