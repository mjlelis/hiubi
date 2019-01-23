from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from core.models import challenge

class ChallangeList(ListView):
    model = challenge
