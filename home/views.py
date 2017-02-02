from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


# The page_not_found() view is overridden by handler404:
# The server_error() view is overridden by handler500:
# The permission_denied() view is overridden by handler403:
# The bad_request() view is overridden by handler400:


def page_not_found_view(request):
    return render(request, 'error.html', {'error_title': 'Page Not Found',
                                          'error_msg': 'Ah oh, you have accidentally stepped into nowhere.'})


def error_view(request):
    return render(request, 'error.html', {'error_title': 'Server Error',
                                          'error_msg': 'What have you done to me?'})


def permission_denied_view(request):
    return render(request, 'error.html', {'error_title': 'Permission Denied',
                                          'error_msg': 'It seems that you are not doing it in the right way.'})


def bad_request_view(request):
    return render(request, 'error.html', {'error_title': 'Bad Request',
                                          'error_msg': 'The request you have sent is too difficult for me to understand.'})


