from django.contrib.auth.models import Group

def is_admin_context(request):
    is_admin = False
    if request.user.is_authenticated:
        is_admin = Group.objects.filter(name='admins').exists() and request.user.groups.filter(name='admins').exists()
    return {'is_admin': is_admin}