from django.db import models
from django.urls import reverse

MOVEMENTS = (
    ('', ''),
    ('M', 'Mechanical'),
    ('Q', 'Quartz'),
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('accessory_detail', kwargs={'accessory_id': self.id})

# Create your models here.
class Watch(models.Model):
    make = models.CharField(max_length=100, default='')
    model_name = models.CharField(max_length=100, default='')
    model_ref = models.CharField(max_length=100, default='')
    serial_number = models.CharField(max_length=100)
    band_width = models.IntegerField(default=0)
    band_type = models.CharField(max_length=100, default='')
    band_color = models.CharField(max_length=100, default='')
    case_diameter = models.IntegerField(default=0)
    case_material = models.CharField(max_length=100, default='')
    other_materials = models.CharField(max_length=100, default='')
    watchface_color = models.CharField(max_length=100, default='')
    movement = models.CharField(
        max_length=100,
        choices=MOVEMENTS,
        default=MOVEMENTS[0][0],
    )
    thickness = models.FloatField(default=0.00)
    weight = models.FloatField(default=0.00)
    notes = models.TextField(default='')
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} with a {self.get_movement_display()} movement."
    
    def get_absolute_url(self):
        return reverse('watches_detail', kwargs={'watch_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)

    def __str__(self):
        return self.url