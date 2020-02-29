from django.db import models

# Create your models here.


class RunoDB(models.Model):
    picture = models.CharField(max_length=64, blank=True)
    name = models.CharField(max_length=64)
    caption = models.TextField(max_length=480, blank=True)
    author = models.CharField(max_length=32, blank=True)
    rate = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.name


class RunoRate(models.Model):
    text = models.CharField(max_length=64, blank=True)
    rate = models.ForeignKey(RunoDB, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Kirjoittaja(models.Model):
    name = models.CharField(max_length=64)
    age = models.CharField(max_length=3, blank=True)
    runodb_id = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.name


class Valokuva(models.Model):
    picture = models.CharField(max_length=64, blank=True)
    kirjoittaja = models.ForeignKey(Kirjoittaja, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture


class Elokuva(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Kaveri(models.Model):
    name = models.CharField(max_length=64)
    elokuvat = models.ManyToManyField(Elokuva)

    def __str__(self):
        return self.name

