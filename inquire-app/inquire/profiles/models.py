from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from inquire.profiles.constants import *
from inquire.profiles.managers import InquireUserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), db_index=True, unique=True)
    first_name = models.CharField(_('First name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last name'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    object_type = "profile"
    objects = InquireUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ("id",)

    def get_short_name(self):
        return self.first_name
