from django.shortcuts import render, redirect, HttpResponse
from blog_app.models import Settings, NavbarModel, Footer, PostModel, PostImageModel, PostContactModel
from .forms import PostContactForm, PostCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog_project.settings import EMAIL_HOST_USER
from blog_app.signals import user_verify
from django.contrib import messages

User = get_user_model()


# Create your views here.
@login_required(login_url='login_page')
def home_view(request):
    context = {}
    posts_queryset = PostModel.objects.filter(is_activate=True)
    context['posts_queryset'] = posts_queryset
    return render(request, 'index.html', context)


def post_detail_view(request, post_id):
    context = {}
    post_detail_queryset = PostModel.objects.filter(id=post_id).first()
    post_detail_images = PostImageModel.objects.filter(post_id=post_id)
    context['post_detail_queryset'] = post_detail_queryset
    context['post_detail_images'] = post_detail_images
    return render(request, 'post_detail.html', context)


def post_contact_view(request):
    context = {}
    form = PostContactForm()
    if request.method == 'POST':
        form = PostContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')
        else:
            context['form'] = form
            return render(request, 'contact.html', context)

    context['form'] = form
    return render(request, 'contact.html', context)


def post_create_view(request):
    context = {}
    form = PostCreateForm()
    if request.method == 'POST':
        images = request.FILES.getlist("images_all")
        form_new = PostCreateForm(request.POST, request.FILES)
        if form_new.is_valid():
            forms = form_new.save(commit=False)
            forms.user_id = request.user
            forms.save()
            for i in images:
                PostImageModel.objects.create(
                    post_id_id=forms.id,
                    images=i
                )

            return redirect('home_page')
        else:

            context['form'] = form_new
            messages.error(request, form_new.errors)
            return render(request, 'post_create.html', context)

    context['form'] = form
    return render(request, 'post_create.html', context)


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            context['form'] = form
            messages.error(request, form.errors)
            return render(request, 'register.html', context)

    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'register.html', context)


def login_view(request):
    context = {}
    username = request.POST.get('username')
    raw_password = request.POST.get('password')
    user = authenticate(username=username, password=raw_password)
    if user:
        login(request, user)
        return redirect('home_page')
    else:
        context['error_message'] = "ERROR"
        return render(request, 'login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('login_page')


def send_test_mail(request):
    user_verify(created=True, instance=request)
    return HttpResponse("Ugurla gonderildi")


def post_update_view(request, post_id):
    context = {}
    update_data = PostModel.objects.filter(id=post_id).first()
    form = PostCreateForm(instance=update_data)

    if request.method == 'POST':
        images = request.FILES.getlist("images_all")
        form_new = PostCreateForm(request.POST, instance=update_data)
        if form_new.is_valid():
            form_new.save()
            for i in images:
                PostImageModel.objects.update(
                    post_id_id=form_new.id,
                    images=i
                )

            return redirect('home_page')
        else:

            context['form'] = form_new
            messages.error(request, form_new.errors)
            return render(request, 'post_create.html', context)

    context['form'] = form
    context['post_id'] = update_data
    return render(request, 'post_update.html', context)


def post_delete_view(request, post_id):
    post_delete = PostModel.objects.filter(id=post_id).first()
    post_delete.delete()
    return redirect('home_page')
