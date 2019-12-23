from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
import boto3
import uuid
from .models import Watch, Accessory, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com'
BUCKET = 'watchcollector-1396'

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

class WatchList(LoginRequiredMixin, ListView):
    model = Watch
    fields = '__all__'
    context_object_name = 'watch_list'

class WatchCreate(LoginRequiredMixin, CreateView):
    model = Watch
    fields = '__all__'
    success_url = '/watches/'

class WatchDetail(LoginRequiredMixin, DetailView):
    model = Watch
    fields = '__all__'

class WatchUpdate(LoginRequiredMixin, UpdateView):
    model = Watch
    fields = '__all__'
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

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

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