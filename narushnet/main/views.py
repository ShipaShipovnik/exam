from .models import Application,CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegistrationForm,ApplicationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

#главная
def index(request):
    return render(request,'main/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #аутентификация
            login(request,user)
            return redirect('user_profile')
    else:
        form = RegistrationForm()
    return render(request,'main/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return redirect('home')
@login_required
def user_profile(request):
    user = request.user
    applications = Application.objects.filter(user=user)
    context = {
        'user':user,
        'applications':applications,
    }
    return render(request, 'main/userprofile.html', context);

# ====================================================================================================
def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('user_profile')
    else:
        form = ApplicationForm()
    return render(request,'main/add.html',{'form':form})

#проверка
def is_admin(user):
    return user.groups.filter(name='admins').exists()

#список----------
@user_passes_test(is_admin)
def some_view(request):
    context = {
        'is_admin': is_admin(request.user),
        # другие данные контекста
    }
    return render(request, 'your_template.html', context)

@user_passes_test(is_admin)
def application_list(request):
    applications = Application.objects.all()
    return render(request, 'main/application-list.html', {'applications': applications})

#кнопки----------
@user_passes_test(is_admin)
def reject_application(request,application_id):
    application = get_object_or_404(Application,id=application_id)
    application.status = 'rejected'
    application.save()
    return redirect('application_list')

@user_passes_test(is_admin)
def approve_application(request,application_id):
    application = get_object_or_404(Application,id=application_id)
    application.status = 'approved'
    application.save()
    return redirect('application_list')




