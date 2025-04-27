from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Mahsulot nomi')
    description = models.TextField(verbose_name='Tavsif')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')
    image = models.ImageField(upload_to='products/', verbose_name='Rasm')
    category = models.CharField(max_length=100, verbose_name='Kategoriya')
    stock = models.IntegerField(default=0, verbose_name='Soni')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
