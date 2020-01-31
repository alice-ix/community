from django.contrib import admin
from django.urls import path, include
from alice_user.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alice_user/', include('alice_user.urls')),
    path('', home),
]
