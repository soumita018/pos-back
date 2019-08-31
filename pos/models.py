from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,name,phone,password=None):
        if not email:
            raise ValueError("Enter your email")
        if not phone:
            raise ValueError("Enter your phone")
        if not name:
            raise ValueError("Enter your name")
        
        user = self.model(email=self.normalize_email(email),phone=phone,name=name)
        user.set_password(password)
        user.is_admin=False
        user.is_staff=False
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,phone,password):
        user=self.create_user(email=email,name=name,phone=phone,password=password)
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


USER_TYPE = (('Admin','Admin'),('Stuff','Stuff'))
ORDER_STATUS_CHOICES = (('Order Received','Order Received'),('Processing','Processing'),('Delivered','Delivered'))

class Restaurant(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    resturant = models.ForeignKey(Restaurant,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    resturant = models.ForeignKey(Restaurant,blank=True,null=True,on_delete=models.CASCADE)
    cat_name = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    resturant = models.ForeignKey(Restaurant,blank=True,null=True,on_delete=models.CASCADE)
    cat_name = models.ForeignKey(Category,blank=True,null=True,on_delete=models.CASCADE)
    sub_cat_name = models.ForeignKey(SubCategory,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True,max_length=200)
    price = models.IntegerField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    slug = models.SlugField(max_length=100, db_index=True,verbose_name=u'Slug(Do not edit if it is already generated!)')
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    def thumb(self):
        if self.image:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.image.url))
        else:
            return u'No image file found'



class User(AbstractBaseUser,PermissionsMixin):
    resturant = models.ForeignKey(Restaurant,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True,max_length=200)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be 10 digits and entered in the format: '9775876662'.")
    phone = models.CharField(validators=[phone_regex],blank=True,null=True, max_length=10,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    user_type = models.CharField(default='Stuff',max_length=100,choices=USER_TYPE,verbose_name=u"User Type")

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name','email']

    def __str__(self):
        return self.phone

class Customer(models.Model):
    name = models.CharField(max_length=300,blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be 10 digits and entered in the format: '9775876662'.")
    phone = models.CharField(validators=[phone_regex],blank=True,null=True, max_length=10,unique=True)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    customer = models.ForeignKey(Customer,blank=True,null=True,on_delete=models.CASCADE)
    resturant = models.ForeignKey(Restaurant,blank=True,null=True,on_delete=models.CASCADE)
    order_total = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(max_length=160,default='Order Received',choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return self.customer.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order,blank=True,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.product.name
    
    











