from django.urls import path
from .views import detail, new_item, delete, edit

app_name = 'item'


urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/edit', edit, name='edit'),
    path('<int:pk>/delete', delete, name='delete'),
    path('new/', new_item, name='new'),
]