from django.urls import path
from projects import views
# from djangoProject_realpython

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:pk>', views.project_detail, name='project_detail')
    # path('test', views.project_list),
]
