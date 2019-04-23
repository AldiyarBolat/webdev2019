from django.urls import path, re_path
from api import views

urlpatterns = [
    path('api/task_lists', views.task_lists),
    re_path(r'api/task_lists/(\d)/tasks', views.task_lists_tasks),
    re_path(r'api/task_lists/(\d)', views.task_list),

    path('api/tasks', views.tasks),
    re_path(r'api/task/(\d)', views.TaskView.as_view()),

    path('api/users/', views.UserList.as_view()),
    path('api/login/', views.login)
]
