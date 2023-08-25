from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, about, contact, signup
from .forms import LoginForm

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view( template_name='core/login.html', authentication_form=LoginForm), name='login'),
]