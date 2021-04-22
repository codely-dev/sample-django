from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField('Anzeigebild', upload_to='locations', default='default.jpg')
    description = models.TextField('Beschreibung', blank=True)
    fluggebiet_image = models.ImageField('Fluggebiet Bild', upload_to='locations', blank=True, null=True)
    landevolte_description = models.TextField('Landevolte', blank=True)
    landevolte_image = models.ImageField('Landevolte Bild', upload_to='locations', blank=True, null=True)
    komoot = models.IntegerField('Aufstiegsroute (Komoot TourId)', blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        # Delete Image when object is deleted.
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        return str(self.title)