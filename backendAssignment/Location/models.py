from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
from django.db import models
from django.forms import ValidationError

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    '''
    Custom User Model
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

class Country(models.Model):
    '''
    Country Model
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(name='name', max_length=50)
    country_code = models.CharField(name='country_code', max_length=10)
    curr_symbol = models.CharField(max_length=10) 
    phone_code = models.CharField(name="phone_code", max_length=10)
    my_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Country'
        managed = True
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        

class State(models.Model):
    '''
    State Model
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(name='name', max_length=50)
    state_code = models.CharField(name='state_code', max_length=10)
    gst_code = models.CharField(name="gst_code", max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'State'
        managed = True
        verbose_name = 'State'
        verbose_name_plural = 'States'
        unique_together = ('name', 'my_country')



class City(models.Model):
    '''
    City Model
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(name='name', max_length=50)
    city_code = models.CharField(name='city_code', max_length=10)
    population = models.IntegerField()
    avg_age = models.FloatField()
    num_of_adult_males= models.IntegerField()
    num_of_adult_females = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'City'
        managed = True
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        unique_together = ('name', 'my_state'), ('city_code', 'my_state')
    
    def clean(self):
        if self.population <= self.num_of_adult_males + self.num_of_adult_females:
            raise ValidationError('Population must be greater than the sum of the number of adult males and females.')