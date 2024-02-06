from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название'
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id',)


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        verbose_name='Пользователь',
        default=None
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Оплачено'
    )
    status = models.CharField(
        max_length=50,
        default='В обработке',
        verbose_name='Статус заказа'
    )

    class Meta:
        db_table = 'order'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.SET_DEFAULT,
        null=True,
        verbose_name='Продукт',
        default=None
    )
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата продажи'
    )

    class Meta:
        db_table = 'order_item'
        verbose_name = 'проданный товар'
        verbose_name_plural = 'проданные товары'
