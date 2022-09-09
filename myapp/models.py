from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."


class MyPerson(Person):

    class Meta:

        proxy = True

    def do_something(self):
        # ...
        pass


class Musician(Person):
    instrument = models.CharField(max_length=100)
    salary = models.FloatField(null=True)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko's blog":
            return  # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.


class School(models.Model):
    institution = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Student(School):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Snack_Bar(Place):
    serves_snacks = models.BooleanField(default=False)
    serves_drinks = models.BooleanField(default=False)
