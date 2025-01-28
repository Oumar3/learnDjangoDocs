
from django.db import models
from django.forms import ValidationError

# Create your models here.

class Category(models.Model):
    name = models.CharField('nom de la categorie',max_length=100,help_text='le nom de la categorie')

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(categorie__isnull=False)

class blog(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blog/',blank=True)
    

    def __str__(self):
        return self.name
    def delete(self):
      self.img.delete()
      super().delete()

class Product(models.Model):
    objects = ProductManager()
    categorie = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name='categorie du produit',related_name='product')
    name = models.CharField('nom du produit',max_length=100,help_text='le nom du produit')
    description = models.TextField('la description de produit')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.name == '' or self.name is None or len(self.name) <= 3:
            raise ValidationError('Le nom du produit ne peut pas être vide')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class status(models.TextChoices):
    en_attente = 'en attente'
    servi = 'servi'
    refuse = 'refuse'

class demande(models.Model):
    client = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='client')
    produit = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='produit demandé')
    quantite = models.IntegerField(verbose_name='quantité')
    status = models.CharField(max_length=10,choices=status.choices,default='en attente')
    date = models.DateField(verbose_name='date')

    def __str__(self):
        return self.produit.name
    
class en_attente(demande):
    class Meta:
        proxy = True
        verbose_name = 'demande en attente'
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='en attente')
    objects = Manager()

    def save(self, *args, **kwargs):
        if self._state.adding:
            raise ValidationError('Le produit ne peut pas être vide')
        return super().save(*args, **kwargs)

class servi(demande):
    class Meta:
        proxy = True
        verbose_name = 'demande servi'
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='servi')
    objects = Manager()

class refuse(demande):
    class Meta:
        proxy = True
        verbose_name = 'demande refusée'
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='refuse')
    objects = Manager()