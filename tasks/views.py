from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def base_page(request):
    return render(request, 'tasks/base.html')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # تسک‌های مرتبط با کاربر جاری
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# اضافه کردن تسک جدید
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

# ویرایش تسک
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

# حذف تسک
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره اطلاعات کاربر
            return redirect('login')  # پس از ثبت‌نام، کاربر به صفحه ورود هدایت می‌شود
    else:
        form = RegisterForm()  # در صورت درخواست GET، فرم خالی نمایش داده می‌شود

    return render(request, 'tasks/register.html', {'form': form})
