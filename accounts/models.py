from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from superuser.models import Department

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email, password=None , **extra_fields):
    
        if email is None:
            raise TypeError('Email Field Must Be Required')
        

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email = email,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, password =None , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser field is_staff must be True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser field is_super must be True')

        return self.create_user(email=email, password=password, **extra_fields)



class Account(AbstractBaseUser,PermissionsMixin):

    USER_TYPES = [
        ('admin' , 'Admin'),
        ('user', 'User'),
    ]

    first_name      = models.CharField(max_length=100, blank=True)
    last_name       = models.CharField(max_length=100, blank=True)
    email           = models.EmailField(max_length=200, unique=True, db_index=True, null=False)
    phone_number    = models.CharField(max_length=14,blank=True)
    role            = models.CharField(default='user',max_length=200, choices=USER_TYPES, blank=True)
    department      = models.ForeignKey(Department, on_delete=models.PROTECT , null=True)
    is_verified     = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    created_by      = models.CharField(default='user' , choices=USER_TYPES , max_length=200 , blank=True)
    created_at      = models.DateField(auto_now_add=True)
    updated_at      = models.DateField(auto_now=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name']


    objects = AccountManager()

    def __str__(self):
        return self.email