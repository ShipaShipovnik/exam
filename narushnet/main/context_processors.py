from django.contrib.auth.models import Group

def user_in_admin_group(request):
    if request.user.is_authenticated:
        is_admin = Group.objects.get(name='admins').user_set.filter(id=request.user.id).exists()
    else:
        is_admin = False
    return {'is_admin': is_admin}
