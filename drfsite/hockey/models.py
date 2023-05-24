from django.db import models


class Hockey(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    namber = models.IntegerField(blank=None)
    position = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    img = models.URLField()
    Idplayer = models.OneToOneField('Player', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.type


class Player(models.Model):
    age = models.IntegerField(blank=None)
    gr = models.ForeignKey('Grips', on_delete=models.PROTECT, null=True)
    sc = models.ForeignKey('SportsCitizenship', on_delete=models.PROTECT, null=True)


class SportsCitizenship(models.Model):
    SC = models.CharField(max_length=255)

    def __str__(self):
        return self.SC


class Grips(models.Model):
    grips = models.CharField(max_length=255)

    def __str__(self):
        return self.grips


class Trener(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img = models.URLField()
    Idpost = models.ForeignKey('Post', on_delete=models.PROTECT, null=True)


class Post(models.Model):
    post = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.post


class Staff(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img = models.URLField()
    idprof = models.ForeignKey('Prof', on_delete=models.PROTECT, null=True)


class Prof(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.type


class Guide(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    img = models.URLField()
    idprof = models.ForeignKey('Posts', on_delete=models.PROTECT, null=True)


class Posts(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.type


class Articles(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)


class PressService(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    idprof = models.ForeignKey('ProfPress', on_delete=models.PROTECT, null=True)


class ProfPress(models.Model):
    type = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.type


