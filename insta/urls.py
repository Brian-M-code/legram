from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

from .views import HomePageView, ProfilePageView

urlpatterns = [
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('', HomePageView.as_view(), name='home')
]

