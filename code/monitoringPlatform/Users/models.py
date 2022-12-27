from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager( BaseUserManager ):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User( AbstractBaseUser ):
    username = None

    email = models.EmailField(('Email address'), unique=True)

    name = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    cpf = models.CharField(
        max_length=14,
        blank=False,
        null=False
    )

    phone_number = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    objects = UserManager()

    # Change the field username for email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Admin( User ):

    def authenticateProfessional() :
        ...



class Client ( User ):
    ...



class Professional( User ):
    validator_code = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    place_of_care = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    NUTRITIONIST = 'N'
    PHYSICAL_EDUCATOR = 'PE'

    PROFESSIONAL_TYPE_CHOICES = [
        (NUTRITIONIST, 'NUTRITIONIST'),
        (PHYSICAL_EDUCATOR, 'PHYSICAL EDUCATOR'),
    ]

    professional_type =  models.CharField(
        max_length=2,
        choices= PROFESSIONAL_TYPE_CHOICES,
        default=NUTRITIONIST,
        blank=False,
        null=False
    )
    
    # by default, professional is not authenticated
    authenticated =  models.BooleanField(
        default=False,
        blank=True,
        null=False
    )


class AuthenticateRequest( models.Model ):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE
    )

    request_date = models.DateTimeField(
        auto_now_add=True
    )
