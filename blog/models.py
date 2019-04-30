from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField("Titre", max_length=255)
    created_date= models.DateTimeField("Date de création",
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    text = models.TextField("Texte")
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
