from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


# All the routing of the website patterns
urlpatterns = [

    # Url for users authentications
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    
    # Default homepage url of the website
    path("", views.index, name="index")
]


# Setting for adding the media in our app
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)