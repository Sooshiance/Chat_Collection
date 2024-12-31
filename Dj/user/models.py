from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class AllUser(BaseUserManager):
    def create_user(self, phone, username, password=None):
        if not username:
            raise ValueError("کاربر باید پست الکترونیکی داشته باشد")

        if not phone:
            raise ValueError("کاربر باید شماره تلفن داشته باشد")

        user = self.model(
            phone=phone,
            username=username,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, username, password):
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_active = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password):
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(
        r"^[0-9a-zA-Z]*$", message="فقط نمادهای الفبایی و اعداد پذیرفته میشوند"
    )
    numbers = RegexValidator(r"^[0-9a]*$", message="تنها اعداد پذیرفته میشوند")
    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[numbers],
        verbose_name="شماره تماس",
        help_text="این فیلد برای احراز هویت استفاده میشود، در انتخاب آن دقت کنید",
    )
    username = models.CharField(max_length=11, unique=True, verbose_name="نام کاربری")
    is_active = models.BooleanField(
        default=True, null=False, verbose_name="وضعیت فعالیت"
    )
    is_staff = models.BooleanField(
        default=False, null=False, verbose_name="دسترسی ادمین"
    )
    is_superuser = models.BooleanField(default=False, null=False, verbose_name="مدیر")

    objects = AllUser()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.phone}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        managed = True
        verbose_name = "User"
        verbose_name_plural = "Users"
