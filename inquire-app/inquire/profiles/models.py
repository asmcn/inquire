from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from readng.profiles.constants import *
from readng.profiles.managers import ReadngUserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), db_index=True, unique=True)
    first_name = models.CharField(_('First name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last name'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    object_type = "profile"
    objects = ReadngUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ("id",)

    def get_short_name(self):
        return self.first_name


class ConnectedAccount(models.Model):
    profile = models.ForeignKey(UserProfile, verbose_name=_("Profile"), related_name="connected_accounts")
    service = models.CharField(_("Service"), choices=SERVICE_CHOICES, max_length=255)
    identifier = models.CharField(_("Service Identifier"), max_length=255, db_index=True)
    service_token = models.TextField(_("Service Token"), blank=True)

    class Meta:
        verbose_name = _("Connected Account")
        verbose_name_plural = _("Connected Accounts")
        unique_together = ("service", "identifier")

    def __unicode__(self):
        return "%s account of %s" % (self.service, self.profile)
