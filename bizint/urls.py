from django.urls import path

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
]
