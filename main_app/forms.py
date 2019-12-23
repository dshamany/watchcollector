from django.forms import ModelForm
from .models import Watch, Accessory

class WatchForm(ModelForm):
    class meta:
        model = Watch
        fields = '__all__'

class AccessoryForm(ModelForm):
    class meta:
        model = Accessory
        fields = '__all__'