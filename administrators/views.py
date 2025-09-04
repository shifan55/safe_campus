import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from students.models import Report
from django.db.models import Count
from django.utils import timezone

def is_admin(u): return hasattr(u, 'administratorprofile') or u.is_superuser

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    total = Report.objects.count()
    status_counts = Report.objects.values('status').annotate(c=Count('id'))
    labels = [x['status'] for x in status_counts] or ['New','In Progress','Closed']
    values = [x['c'] for x in status_counts] or [0,0,0]
    chart = {'labels': labels, 'datasets':[{'label':'Reports by Status','data': values}]}
    return render(request, 'administrators/dashboard.html', {'total_reports': total, 'chart_json': json.dumps(chart)})

@login_required
@user_passes_test(is_admin)
def assign_report(request, report_id):
    # stub assignment page
    from django.contrib.auth.models import User
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        counselor_id = request.POST.get('counselor_id')
        if counselor_id:
            report.assigned_counselor = get_object_or_404(User, pk=counselor_id)
            report.save()
            return redirect('administrators:dashboard')
    counselors = User.objects.filter(counselorprofile__isnull=False)
    return render(request, 'administrators/assign.html', {'report': report, 'counselors': counselors})
