from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .base_models import BaseModel
from managers.user_manager import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
