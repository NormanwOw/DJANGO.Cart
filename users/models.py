from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table = 'user'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
