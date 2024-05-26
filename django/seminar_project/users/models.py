from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, ID, name, password=None, generation=None, gender=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not ID:
            raise ValueError('Users must have an ID')
        
        user = self.model(
            email=self.normalize_email(email),
            ID=ID,
            name=name,
            generation=generation,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, ID, name, password=None, generation=None, gender=None):
        user = self.create_user(
            email,
            ID=ID,
            name=name,
            password=password,
            generation=generation,
            gender=gender,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    ID = models.CharField(max_length=30, unique=True, primary_key=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    name = models.CharField(max_length=30)
    generation = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'ID'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.ID

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
