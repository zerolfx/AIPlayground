from django import forms
from .models import User, UserProfile
from django.contrib.auth import authenticate


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['email'].required = True

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'birth_date',
                  'country', 'city', 'organization']


def validator(get_data, action_type):
    response = {'message': [], 'error': []}
    username = get_data['username']
    password = get_data['password']
    if action_type and username and password:
        if len(username) < 4:
            response['error'] = 'Username is too short.'
        if len(username) > 20:
            response['error'] = 'The length of username should not exceed 20.'
        if len(password) < 6:
            response['error'] = 'Password is too short.'
        if response['error']:
            return response
        if action_type == 'register':
            if forbidden_username_validator(username):
                response['error'] = 'Username already exists.'
            elif User.objects.filter(username=username).exists():
                response['error'] = 'Username already exists.'
            else:
                new_user = User.objects.create_user(username=username, password=password)
                UserProfile.objects.create(user=new_user, email=get_data['email'])
                response['message'] = 'Register success, redirecting now...'
        elif action_type == 'login':
            login_user = authenticate(username=username, password=password)
            if login_user:
                response['message'] = 'Login success, redirecting now...'
            else:
                response['error'] = 'Invalid username or password.'
    if not response['error'] and not response['message']:
        response['error'] = 'Please enter username and password.'
    return response


def forbidden_username_validator(value):
    forbidden_username = ['admin', 'settings', 'news', 'about', 'help',
                          'signin', 'signup', 'signout', 'terms', 'privacy',
                          'cookie', 'new', 'login', 'logout', 'administrator',
                          'join', 'account', 'username', 'root', 'blog',
                          'user', 'users', 'billing', 'subscribe', 'reviews',
                          'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                          'home', 'job', 'jobs', 'contribute', 'newsletter',
                          'shop', 'profile', 'register', 'auth',
                          'authentication', 'campaign', 'config', 'delete',
                          'remove', 'forum', 'forums', 'download',
                          'downloads', 'contact', 'blogs', 'feed', 'feeds',
                          'faq', 'intranet', 'log', 'registration', 'search',
                          'explore', 'rss', 'support', 'status', 'static',
                          'media', 'setting', 'css', 'js', 'follow',
                          'activity', 'questions', 'articles', 'network', ]

    return value.lower() in forbidden_username
