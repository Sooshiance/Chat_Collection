from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser, PermissionsMixin


class AllUser(BaseUserManager):
    def create_user(self, username, phone, password=None, first_name=None, last_name=None):
        if not phone:
            raise ValueError("Need Phone")
        
        if not username:
            raise ValueError("Need Username")
        
        if not first_name:
            raise ValueError("Need Name")
        
        if not last_name:
            raise ValueError("Need Family Name")

        user = self.model(
            phone=phone,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    numbers      = RegexValidator(r'^09\d{9}$', message="Numbers")
    phone        = models.CharField(unique=True, max_length=244, validators=[numbers])
    username     = models.CharField(max_length=11, unique=True)
    first_name   = models.CharField(max_length=30, null=True, blank=True)
    last_name    = models.CharField(max_length=50, null=True, blank=True)
    is_active    = models.BooleanField(default=True, null=False)
    is_staff     = models.BooleanField(default=False, null=False)
    is_superuser = models.BooleanField(default=False, null=False)

    objects = AllUser()

    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return f"{self.phone}"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ['phone', 'username']


class OTP(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    otp        = models.CharField(max_length=6)
    counter    = models.PositiveSmallIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'
