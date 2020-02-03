from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class MainPageView(View):
    def get(self, request, params=None):
        return render(request, 'test_app/index.html')