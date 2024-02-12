from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    """
    after the sign up form is submitted, user
    will be redirected to the login page
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
