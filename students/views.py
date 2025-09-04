from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report

def report_form(request):
    if request.method == 'POST':
        desc = request.POST.get('description','').strip()
        lat = request.POST.get('location_lat') or None
        lng = request.POST.get('location_lng') or None
        rep = Report.objects.create(
            description=desc,
            location_lat=float(lat) if lat else None,
            location_lng=float(lng) if lng else None,
            reporter=request.user if request.user.is_authenticated else None,
            is_anonymous= not request.user.is_authenticated
        )
        return redirect('students:report_thanks')
    return render(request, 'students/report_form.html')

def report_thanks(request):
    return render(request, 'students/report_thanks.html')

@login_required
def dashboard(request):
    my_reports = Report.objects.filter(reporter=request.user)
    return render(request, 'students/dashboard.html', {'my_reports': my_reports})
