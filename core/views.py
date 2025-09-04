from django.shortcuts import render, redirect
def home(request):
    # Redirect authenticated users by simple role heuristics
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'administratorprofile'):
            return redirect('administrators:dashboard')
        if hasattr(user, 'counselorprofile'):
            return redirect('counselors:dashboard')
        if hasattr(user, 'studentprofile'):
            return redirect('students:dashboard')
    return render(request, 'core/home.html')
