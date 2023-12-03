from django.shortcuts import render
from django.views import View
from .models import FAQ

class faq_view(View):
    def get(self, request):
        faqs = FAQ.objects.all()
        return render(request, 'faq_page.html', {'faqs': faqs})