from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'bizint'
urlpatterns = [
    # ex: /bizint/
    path('', views.index, name='index'),
    # ex: /bizint/5
    path('<int:action_id>/', views.info, name='info'),
    # ex: /bizint/5/add
    path('<int:action_id>/add', views.add, name='add'),
    # ex: /api/actions
    path('api/actions', views.api_actions, name='api_actions'),
    path('login/', auth_views.LoginView.as_view(template_name='bizint/login.html'), name='login')
]
