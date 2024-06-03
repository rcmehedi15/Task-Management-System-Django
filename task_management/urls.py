from django.contrib import admin
from django.urls import path, include
from task import views as task_views  # Import the task views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='home'),  # Set the default route to task_list view
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
