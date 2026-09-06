from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="دسته‌بندی"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="نام غذا"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    price = models.PositiveIntegerField(
        verbose_name="قیمت"
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="عکس غذا"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="موجود است"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"

    def __str__(self):
        return self.name


class RestaurantInfo(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="نام رستوران"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    hero_title = models.CharField(
        max_length=200,
        default="Taste the Difference",
        verbose_name="عنوان اصلی"
    )

    hero_subtitle = models.TextField(
        blank=True,
        verbose_name="متن اصلی"
    )

    hero_image = models.ImageField(
        upload_to="restaurant/",
        blank=True,
        null=True,
        verbose_name="عکس اصلی"
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="شماره تماس"
    )

    address = models.TextField(
        blank=True,
        verbose_name="آدرس"
    )

    instagram = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="اینستاگرام"
    )

    class Meta:
        verbose_name = "اطلاعات رستوران"
        verbose_name_plural = "اطلاعات رستوران"

    def __str__(self):
        return self.name