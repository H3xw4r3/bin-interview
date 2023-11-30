from django.urls import path
from .views import puResult, index, lga_result, addResult

urlpatterns = [
    path('', index, name='home'),
    path('result/<int:pu_id>', puResult, name='pu_result'),
    path('result/lga', lga_result, name='lga_result' ),
    path('result/add/', addResult, name="addResult",)
]