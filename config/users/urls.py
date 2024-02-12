from django.urls import path
from .views import SignupPageView


urlpatterns = [
        # sign up page
        path('signup/', SignupPageView.as_view(), name='signup'),
]
