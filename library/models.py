from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    year=models.DateField(null=True, blank=True)
    biografy=models.TextField(null=True, blank=True)

    class Meta:
        verbose_name="Автор"
        verbose_name_plural="Автор"

    def __str__(self):
        return self.name



class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    publish_year=models.PositiveIntegerField()
    authors=models.ManyToManyField(Author, related_name='Авторы')

    class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книга"

    def __str__(self):
        return self.title


class Feedback(models.Model):
    full_name=models.CharField("ФИО", max_length=100)
    feedback=models.CharField("Отзыв",max_length=200)
    book=models.ManyToManyField(Book, related_name="Книга")

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзыв"

    def __str__(self):
        return self.full_name



