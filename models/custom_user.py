from django.utils.translation import gettext_lazy as _

from .base_models import BaseModel
from managers.user_manager import UserManager

from django.contrib.auth.base_user import AbstractBaseUser


class User(BaseModel, AbstractBaseUser):

    
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
