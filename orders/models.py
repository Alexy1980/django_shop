from django.db import models
from products.models import Product

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "Статус: %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


# название модели соответствует названию таблицы в базе данных
class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=1)
    comments = models.TextField(blank=True, null=True, default=None)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       return "Заказ: %s %s" % (self.id, self.status.name)
    # описание
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

# товары в заказе
class ProductInOrder(models.Model):
    # ссылка на заказ
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    # изменяется при create
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # изменяется при update
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # выводим записи по названию полей
    def __str__(self):
       # вместо %s будут подставлены значение
       return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
