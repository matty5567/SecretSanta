from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.views.generic.base import TemplateView


urlpatterns = [

    path('register/', user_views.signup, name='register'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', TemplateView.as_view(template_name='users/profile.html'), name='profile'),
    path('', user_views.home, name=''),
    path('askquestion/', user_views.ContactFormAsk, name='askquestion'),
    path('replyquestion/', user_views.ContactFormReply, name='replyquestion'),
    path('profile/actionUrl', user_views.Randomiser, name ='Randomiser'),
    path('home/', TemplateView.as_view(template_name='users/home.html'), name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
