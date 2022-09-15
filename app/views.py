from itertools import chain

from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import NewUserForm, PostCreateForm, SerchForm
from .models import Post


def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'index/{user.pk}/')
        else:
            messages.error(request, 'invalid login')

    return render(request, template_name='app/auth.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")

        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()

    return render(request=request, template_name="app/registration.html", context={"register_form": form})


@login_required(login_url='login')
def index(request, pk):
    user = User.objects.get(pk=pk)
    # search_form = SerchForm(request.GET)
    # if request.method == 'GET':
    #     if search_form.is_valid():
    #         return redirect('list')
    #     else:
    #         search_form = SerchForm()
    #     return render(request, 'app/index.html', {'search' : search_form})

    subscribers = request.user.subscribers.all()
    followers = request.user.followers.all()
    posts = user.posts.all()

    return render(request,
                  template_name='app/index.html',
                  context={'posts': posts, 'subscribers': subscribers, 'followers': followers, 'user': user})


@login_required(login_url='login')
def list_view(request):
    subscribers = request.user.subscribers.all()
    post = Post.objects.all()
    usere = request.user.username
    print(usere)
    User = get_user_model()
    users = User.objects.all()
    print(users)
    # posts = list(chain(*[subscriber.following.posts.all() for subscriber in subscribers]))
    # print(posts)
    return render(request, template_name='app/list.html', context={'posts': post})


@login_required(login_url='login')
def detail(request, pk):

    post = Post.objects.get(pk=pk)

    return render(request, template_name='app/detail.html', context={"post": post})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        print(form)
        das = form.save(commit=False)
        das.user = request.user
        # if das.is_valid():
        print('post')
        das.save()
        return redirect('index/')
    form = PostCreateForm
    return render(request, 'app/create_post.html', {'form': form})


def search(request):
    search_term = request.GET.get('search_term')

    if search_term is not None:
        user = User.objects.filter(username__icontains=search_term).first()
        print(user)
        if user is not None:
            return render(request, template_name='app/search.html', context={'user': user})
        return HttpResponse('user is not found')

    return HttpResponse('user is not found ')


def logoutView(request):
    logout(request)
    return redirect('login')

