from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base_page, name='base'),  # صفحه اصلی
    path('tasks_list/', views.task_list, name='task_list'),  # صفحه نمایش تسک‌ها
    path('add/', views.add_task, name='add_task'),  # فرم اضافه کردن تسک جدید
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # ویرایش تسک
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # حذف تسک
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
