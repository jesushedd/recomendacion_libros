def check_user_logged(request):
    context = {}
    if request.user.is_authenticated:
            context['logged'] = True
    return context