from django.db import models

class Article(models.Model):
    title = models.CharField('Titel', max_length=32)
    description = models.TextField('Beschreibung',)
    url = models.URLField('URL', blank=True)
    image = models.ImageField(upload_to='news', blank=True, null=True)
    submitted = models.DateField('Erstelldatum', auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        # Delete Image when object is deleted.
        try:
            self.image.storage.delete(self.image.name)
        except:
            pass
        super().delete()
    
    def __str__(self):
        return str(self.title)