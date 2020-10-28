from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField(("カテゴリー"), max_length=50)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name


class Roulette(models.Model):

    title = models.CharField(("タイトル"), max_length=50)
    category = models.ForeignKey(Category, verbose_name=("カテゴリー"), null=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("ルーレット")
        verbose_name_plural = ("ルーレット")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Roulette_detail", kwargs={"pk": self.pk})

class Content(models.Model):

    content_name = models.CharField(("コンテンツ"), max_length=50)
    roulette = models.ForeignKey(Roulette, verbose_name=("ルーレット"), null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("コンテンツ")
        verbose_name_plural = ("コンテンツ")

    def __str__(self):
        return self.content_name





