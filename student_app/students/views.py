# students/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages
from students.forms import ProfileForm, TaskForm
from students.models import Profile, Task

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile updated successfully!')  # Add success message
        return redirect('profile_view')
    return render(request, 'profile.html', {'form': form})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.profile = request.user.profile
        task.save()
        messages.success(request, 'Task created successfully!')  # Add success message
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, 'Task updated successfully!')  # Add success message
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')  # Add success message
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
