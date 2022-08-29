from django.contrib import admin
from django.urls import path
from myapp import views
from django.views.generic import TemplateView, RedirectView
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('product/new', views.ProductView.as_view(new_product=True), name='product_new'),
    path('product/<int:id>', views.ProductView.as_view(), name='product_id'),
    path('product/list', views.ProductView.as_view(list_product=True), name='product_list'),
    path('profile/<int:id>', views.profile_page, name='profile'),
    path('profile/setting', views.ProfileSettingView.as_view(), name='profile_setting'),
]

login_urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            extra_context={
                'pagename': 'Авторизация'
            }
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        "register/",
        RegistrationView.as_view(
            extra_context={
                'pagename': 'Регистрация'
            }
        ),
        name="django_registration_register",
    ),
    path(
        "register/closed/",
        TemplateView.as_view(
            template_name="django_registration/registration_closed.html",
            extra_context={
                'pagename': 'Регистрация'
            }
        ),
        name="django_registration_disallowed",
    ),
    path(
        "",
        RedirectView.as_view(permanent=False),
        name="django_registration_complete",
    ),
]

urlpatterns += login_urlpatterns
