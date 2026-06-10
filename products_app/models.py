from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Наименование")
    country = models.CharField(max_length=MAX_LENGTH, verbose_name="Страна")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to='brands/%Y/%m/%d', null=True, blank=True, verbose_name="Логотип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Flavor(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Вкус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вкус"
        verbose_name_plural = "Вкусы"


class Ingredient(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name="Наименование")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    weight = models.PositiveIntegerField(verbose_name="Вес (г)")
    photo = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True, verbose_name="Фото")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name="Бренд")
    flavors = models.ManyToManyField(Flavor, blank=True, verbose_name="Вкусы")
    ingredients = models.ManyToManyField(Ingredient, through='ProductIngredient', verbose_name="Состав")

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, verbose_name="Ингредиент")
    amount_mg = models.PositiveIntegerField(verbose_name="Количество (мг)")

    def __str__(self):
        return f"{self.product.name} — {self.ingredient.name} {self.amount_mg}мг"

    class Meta:
        verbose_name = "Состав продукта"
        verbose_name_plural = "Состав продуктов"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]
    customer_name = models.CharField(max_length=MAX_LENGTH, verbose_name="Имя покупателя")
    customer_email = models.EmailField(verbose_name="Email")
    customer_phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")

    def __str__(self):
        return f"Заказ №{self.pk} — {self.customer_name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.FloatField(verbose_name="Цена на момент заказа")

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"