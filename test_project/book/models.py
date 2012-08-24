from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publisher')
    authors = models.ManyToManyField('Author', blank=True)

    @classmethod
    def get_schemata_for_model(self):
        return BookSchema.objects.all()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
