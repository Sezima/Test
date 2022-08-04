# School Site

### School Site - сайт для автоматизации школьных процессов.
____
> Реализованы следующие функции
#### 1. Регистрация учителя через сайт(с номером телефона)
#### 2. Логин и пароль
#### 3. CRUD учеников
#### 4. Поиск учеников
____
### Main
> Модели
> 
>+ Учитель
>  + наследуется от AbstractUser
>  + для валидации номера телефона используется "RegexValidator(regex=r"^\+?1?\d{8,15}$")"
>  + для активационного кода использовалось модуль hashlib.   https://docs-python.ru/standart-library/modul-hashlib-python/
> 
>+ Ученик
>+ Школа
>+ Класс
____

> - [ ] Технологии
- Django
- Pillow
- psycopg2-binary
- djangorestframework
- drf-yasg
- django-phonenumber-field
- phonenumbers
- HTTP status

____

> ### Админ панель
~~~python 
class GradeInline(admin.TabularInline):
    model = Grade
    raw_id_fields = ['students']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['teachers', 'name']
    inlines = [GradeInline]

# TabularInline  чтобы в классе был один учитель и много студентов
# Такая же логика со школой (имя школы и много классов)
~~~
____
> ### Сериализаторы 

+ #### Для всех моделей использовали serializers.ModelSerializer

____
> ### Предстставление 

+ #### Для реализации CRUD использовали (viewsets.ModelViewSet)
+ #### Остальные реализованы через (generics.ListAPIView)
+ #### Поиск учеников 
~~~python 
filter_backends = [SearchFilter]
search_fields = ['name']
 #name = имя ученика
 ~~~

____
####
### Account

> Модели
> 
>+ MyUserManager(BaseUserManager)
>+ изменили менеджер удалив email  и добавили телефон номер
____

> Представление 
> 
> + Использовали APIView для регистрации, активационного кода и выход
> + ссылка с активационным кодом приходит в консоль
____

### Swagger

1. requlrements.txt (drf-yasg)
2. settings.py > INSTALLED_APPS = ['drf_yasg']
3. urls главного приложения 
~~~python
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui()),

]
~~~

____
### Django Signals

~~~python
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Student


@receiver(post_save, sender=Student)
def post_save_user(**k):
    print('Ученик создан')

~~~



