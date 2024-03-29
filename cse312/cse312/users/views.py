from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLogInView, LogoutView as BaseLogOutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import AuthenticationForm, UserCreationForm

class FormErrorsContextMixin:
    def get_context_data(self, **kwargs):
        form = kwargs.get('form')
        form_errors = []
        if form is not None:
            for error_list in form.errors.as_data().values():
                for error in error_list:
                    form_errors.extend(error.messages)
        form_errors_str = ' '.join(form_errors)
        return super().get_context_data(**kwargs, form_errors=form_errors_str)


class LogInView(FormErrorsContextMixin, BaseLogInView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


class LogOutView(BaseLogOutView):
    next_page = 'showFeed'


class CreateAccountView(FormErrorsContextMixin, UserPassesTestMixin, CreateView):
    template_name = 'users/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('showProfile')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('showProfile')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Automatically log the user in.
        login(self.request, self.object)
        return response
