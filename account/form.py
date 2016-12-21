from .models import User
from django.contrib.auth import authenticate, login


def validator(post_data):
    response = {'message': [], 'error': []}
    action_type = post_data['type']
    username = post_data['username']
    password = post_data['password']
    if action_type and username and password:
        if len(username) < 4:
            response['error'] = 'username is too short'
        if len(username) > 20:
            response['error'] = 'the length of username should not exceed 20'
        if len(password) < 6:
            response['error'] = 'password is too short'
        if response['error']:
            return response
        if action_type == 'register':
            if forbidden_username_validator(username):
                response['error'] = 'username is reserved'
            elif User.objects.filter(username=username).exists():
                response['error'] = 'username is already exist'
            else:
                User.objects.create_user(username=username, password=password)
                response['message'] = 'register success'
        elif action_type == 'login':
            login_user = authenticate(username=username, password=password)
            if login_user:
                response['message'] = 'login success'
            else:
                response['error'] = 'invalid login'
    if not response['error'] and not response['message']:
        response['error'] = 'please provide username and password'
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
