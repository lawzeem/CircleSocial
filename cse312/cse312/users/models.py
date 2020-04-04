from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superusers must have is_superuser=True')

        return self._create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    user_name = models.CharField('user name', max_length=50, unique=True)
    is_complete = models.BooleanField(
        'complete',
        default=False,
        help_text=(
            'Checks to see if the user profile is complete. '
        ),
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        ordering = ['email']

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_first_name(self):
        return self.first_name

    def get_user_name(self):
        return self.user_name