from django.urls import path
from .views import faq_view

urlpatterns = [
    path('', faq_view.as_view(), name='faq'),
]