from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from account.models import MyUserManager

SEX = (
    ('male', 'м'),
    ('female', 'ж')
)


class Student(models.Model):
    """Ученик"""
    name = models.CharField(max_length=500, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Электронная почта')
    born = models.DateField(verbose_name='Дата рождения')
    grade = models.CharField(max_length=10)
    address = models.CharField(max_length=200, verbose_name='адрес')
    sex = models.CharField(max_length=100, choices=SEX, verbose_name='пол')
    image = models.ImageField(upload_to='images', verbose_name='фото', null=True, blank=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученик'

    def __str__(self):
        return self.name


class Teacher(AbstractUser):
    """Учитель"""
    username = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex],
                                    max_length=16,
                                    unique=True,
                                    verbose_name="Номер телефона")

    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def create_activation_code(self):
        import hashlib
        string = self.phone_number + str(self.id)
        encode_string = string.encode()
        md5_objects = hashlib.md5(encode_string)
        activation_code = md5_objects.hexdigest()
        self.activation_code = activation_code

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учитель'

    def __str__(self):
        return self.username


class Teach(models.Model):
    """Класс"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'

    def __str__(self):
        return self.name


class Grade(models.Model):
    teacher = models.ForeignKey(Teach, on_delete=models.CASCADE, related_name='teacher')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='stud')


class School(models.Model):
    """Школа"""
    name = models.CharField(max_length=300, verbose_name='Наименование школы')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

    def __str__(self):
        return self.name


class SchoolGrade(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_query_name='grade')
    grade = models.ForeignKey(Teach, on_delete=models.CASCADE, related_name='school')




@receiver(post_save, sender=Student)
def post_save_user(**k):
    print(f'Ученик создан')

