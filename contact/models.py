from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from contact.supabase_storage import SupabaseStorage

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"

class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='contacts/', storage=SupabaseStorage())
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner =  models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"