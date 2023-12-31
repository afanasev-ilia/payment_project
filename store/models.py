from django.db import models

CENTS_IN_DOLLAR = 100


class Item(models.Model):
    name = models.CharField(
        'название товара',
        max_length=150,
        help_text='укажите название',
    )
    description = models.TextField(
        'описание товара',
        help_text='добавьте описание товара',
    )
    price = models.IntegerField(
        'цена в центах',
        default=0,
        help_text='укажите цену товара в центах',
    )

    class Meta:
        default_related_name = 'item'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name

    def get_display_price(self) -> int:
        return '{0:.2f}'.format(self.price / CENTS_IN_DOLLAR)
