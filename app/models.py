from django.db import models

# Create your models here.
class Viewer_Data(models.Model):
    mercury = models.BooleanField(verbose_name="Mercury", blank=True)
    venus = models.BooleanField(verbose_name="Venus", blank=True)
    earth = models.BooleanField(verbose_name="Earth", blank=True)
    mars = models.BooleanField(verbose_name="Mars", blank=True)
    jupiter = models.BooleanField(verbose_name="Jupiter", blank=True)
    saturn = models.BooleanField(verbose_name="Saturn", blank=True)
    uranus = models.BooleanField(verbose_name="Uranus", blank=True)
    neptune = models.BooleanField(verbose_name="Neptune", blank=True)
    pluto = models.BooleanField(verbose_name="Pluto", blank=True)
    
    compute_3D = models.BooleanField(verbose_name="Compute in 3D", blank=True)
    
    