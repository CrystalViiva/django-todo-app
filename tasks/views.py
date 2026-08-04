from django.shortcuts import get_object_or_404, render, redirect
from .forms import TaskForm, RegistrationForm, ProfileForm
from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['just_registered'] = True
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('home')
    return render(request, 'create_task.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.none()

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(done=True).count()
    pending_tasks = tasks.filter(done=False).count()
    just_registered = request.session.pop('just_registered', False)

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'just_registered': just_registered,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


def clone(request):
    return render(request, 'clone.html')


def child(request):
    return render(request, 'child.html')


@login_required
def delete_task(request, id):

    task = get_object_or_404(Task, id=id, user=request.user)
    
    if request.method == 'POST' or request.method == 'GET':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('home')


@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_task.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'user': request.user, 'created': created})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "edit_profile.html", {"form": form, "profile": profile, "created": created, "user": request.user})

