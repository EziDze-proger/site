from django.urls import reverse
from django.db import models

# Create your models here.
class ecologiya(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=5,decimal_places=2,blank=False, verbose_name="цена")
    foto = models.ImageField(upload_to='eco_foto/', verbose_name="фото")
    slug = models.SlugField(max_length=16, unique=True, db_index=True, verbose_name="слаг")


    def __str__(self):
        return (self.title + ": " + str(self.price) + " ₽")
    
    def get_absolute_url(self):
        return reverse("post_product", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "экологичесике товары для посудомойки"
        verbose_name_plural = "экологичесике товары для посудомойки но другие"
        ordering = ["price"]

class support(models.Model):
    title = models.CharField(max_length=255, verbose_name="")
    text = models.TextField(blank=True, verbose_name="")
    photo_forms = models.ImageField(upload_to='support/', verbose_name="")

    
