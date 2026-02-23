from django.shortcuts import render, get_object_or_404
from .models import Appeal

def index(request):
    appeals = Appeal.objects.all().order_by("-created_at")
    return render(request, 'Firstpage/first.html', {
        "appeals": appeals,
        "year": 2025
    })

def appeal_detail(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    return render(request, "Firstpage/appeal_detail.html", {
        "appeal": appeal
    })