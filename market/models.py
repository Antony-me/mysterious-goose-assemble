from __future__ import unicode_literals

from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

# class Profile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     first_name=models.CharField(max_length=200, blank=False)
#     last_name=models.CharField(max_length=200, blank=True)
#     photo =CloudinaryField('image', default="https://res.cloudinary.com/dpcrhvllf/image/upload/v1606208498/ouao15vmh1c1wecxm5ir.pngs")
#     bio = models.TextField(default="No Bio..")

#     def __str__(self):
#         return f"{self.last_name}"

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

class Mall(models.Model):
    name = models.CharField(max_length=200, blank=False)
    image =CloudinaryField('image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    location = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.name)

class Shop(models.Model):
    shop_name = models.CharField(max_length=200, blank=False)
    image =CloudinaryField('image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    floor = models.IntegerField(blank=False)
    shop_no = models.CharField(max_length=200, blank=False)
    mall= models.ForeignKey(Mall, on_delete=models.CASCADE, blank=True, null= True)

    def __str__(self):
        return str(self.shop_name)

class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=False)
    image =CloudinaryField('image', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    price = models.IntegerField(blank=False)
    offers = models.TextField(default="None Today")
    shops = models.ForeignKey(Shop, on_delete=models.CASCADE)
    malls = models.ForeignKey(Mall, on_delete=models.CASCADE, null= True)
   
    def __str__(self):
        return str(self.product_name)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)