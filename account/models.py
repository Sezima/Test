from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

