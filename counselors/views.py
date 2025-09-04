from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from students.models import Report

def is_counselor(u): return hasattr(u, 'counselorprofile')

@login_required
@user_passes_test(is_counselor)
def dashboard(request):
    my_reports = Report.objects.filter(assigned_counselor=request.user)
    inbox = Report.objects.filter(assigned_counselor__isnull=True)
    return render(request, 'counselors/dashboard.html', {'my_reports': my_reports, 'inbox': inbox})
