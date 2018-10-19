from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from social_core.backends.oauth import BaseOAuth2
from urllib.parse import urlencode
from .forms import UserForm


class UserFormView(View):
    form_class = UserForm
    template_name = 'basic/register.html'

    def get(self, request):
        form = self.form_class(None)
        source = request.get_full_path().strip('/').capitalize()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.form_class(request.POST)
        source = request.get_full_path().strip('/').capitalize()

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='basic:index')
        return render(request, self.template_name, locals())


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'basic/register.html'

    def get(self, request):
        form = self.form_class(None)
        source = request.get_full_path().strip('/').capitalize()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        source = request.get_full_path().strip('/').capitalize()

        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='basic:index')
        return render(request, self.template_name, locals())


def logout_view(request):
    logout(request)
    return redirect(to='basic:index')


def privacy(request):
    return render(request, "basic/PrivacyPolite.html", locals())


class FacebookOAuth2(BaseOAuth2):
    """GitHub OAuth authentication backend"""
    name = 'facebook'
    AUTHORIZATION_URL = 'https://facebook.com/login/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://facebook.com/login/oauth/access_token'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]

    def get_user_details(self, response):
        """Return user details from GitHub account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://api.facebook.com/user?' + urlencode({
            'access_token': access_token
        })
        return self.get_json(url)


def index(request):
    return render(request, "basic/index.html", locals())


