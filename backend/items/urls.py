from django.urls import path
from .views import *
urlpatterns = [
    path('getroutes/', getRoutes),
    path('category/', majorCategories),
    path('category/<str:category>/', specificMinorCategory),
    path('category/<str:majorcategory>/<str:minorcategory>/', getCategoryItems),
    path('<int:id>/', getItemForDisplay),
    path('<str:method>/<int:id>/', getItemForUpdateOrDelete),
]