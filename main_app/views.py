from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
import boto3
import uuid
from .models import Watch, Accessory, ProfilePhoto, Photo, Service
from .forms import ServiceForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com'
BUCKET = ''

def signup(request):
    error_msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_msg = 'Invalid Credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    watches = Watch.objects.filter(owner=request.user.id)
    if ProfilePhoto.objects.filter(user=request.user.id):
        return render(request, 'main_app/profile.html', {
            'user': user,
            'photos': ProfilePhoto.objects.filter(user=request.user.id),
            'watches': watches
        })
    return render(request, 'main_app/profile.html', {
            'user': user,
            'watches': watches
        })

def profile_edit(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'main_app/profile_edit.html', {
        'user': user
    })

def profile_update(request):
    user = User.objects.get(id=request.user.id)
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    user.save()
    print(dir(user))
    return redirect('profile')

class WatchList(LoginRequiredMixin, ListView):
    model = Watch
    fields = '__all__'
    context_object_name = 'watch_list'

class WatchCreate(LoginRequiredMixin, CreateView):
    model = Watch
    fields = ['name', 'make', 'model_ref', 'serial_number', 'band_width', 'band_type', 'band_color', 'case_diameter', 'case_material', 'other_materials', 'movement', 'thickness', 'weight', 'notes']
    success_url = '/watches/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class WatchDetail(LoginRequiredMixin, DetailView):
    model = Watch
    fields = '__all__'
    form = ServiceForm


class WatchUpdate(LoginRequiredMixin, UpdateView):
    model = Watch
    fields = ['make', 'name', 'model_ref', 'serial_number', 'band_width', 'band_type', 'band_color', 'case_diameter', 'case_material', 'other_materials', 'watchface_color', 'movement', 'thickness', 'weight', 'notes']
    success_url = '/watches/'

class WatchDelete(LoginRequiredMixin, DeleteView):
    model = Watch
    success_url = '/watches/'

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory
    context_object_name = 'accessories'

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = "__all__"
    success_url = '/accessories/'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = '__all__'
    success_url = '/accessories/'

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'



@login_required
def add_service(request, watch_id):
    form = ServiceForm(request.POST)

    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.watch_id = watch_id
        new_service.save()
    return redirect('watch_detail', watch_id=watch_id)

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def watches_index(request):
    watches = Watch.objects.all()
    return render(request, 'watches/index.html', {
        'watches': watches
    })

@login_required
def watches_detail(request, watch_id):
    watch = Watch.objects.get(id=watch_id)
    accessories = Accessory.objects.all()
    return render(request, 'watches/detail.html', {
        'watch': watch,
        'accessories': accessories,
    })

@login_required
def add_photo(request, watch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        file_extension = photo_file.name[photo_file.name.rfind('.'):]
        key = uuid.uuid4().hex[:8] + file_extension

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            photo = Photo(url=url, watch_id=watch_id)
            photo.save()
        except:
            print('Error while uploading file to s3')
    return redirect('watch_detail', watch_id)

@login_required
def add_profile_photo(request):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        file_extension = photo_file.name[photo_file.name.rfind('.'):]
        key = uuid.uuid4().hex[:8] + file_extension

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            photo = ProfilePhoto(url=url, user_id=request.user.id)
            photo.save()
        except:
            print('Error while uploading file to s3')
    return redirect('profile')


def remove_photo(request, watch_id, photo_id):
    Photo.objects.get(id=photo_id).delete()
    return redirect('watch_detail', watch_id)

def remove_profile_photo(request):
    ProfilePhoto.objects.get(user=request.user.id).delete()
    return redirect('profile')
