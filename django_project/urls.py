from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# views
from users import views as user_views
from django.contrib.auth import views as auth_views

# static
from django.conf.urls.static import static

# settings
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('accounts/', include("allauth.urls")),
    path('signup/', user_views.register, name='user-register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='notes/logout.html'), name='logout'),
    url(r'^comments/', include('django_comments.urls')),
]
if (settings.DEBUG == True):     
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)