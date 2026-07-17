from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
    upload_to="services/",
    max_length=255,
    blank=True,
    null=True
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name



class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
    upload_to="projects/",
    max_length=255,
    blank=True,
    null=True
)

    completed_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title



class Gallery(models.Model):

    title = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
    upload_to="gallery/",
    max_length=255
     )

    category = models.CharField(
        max_length=50
    )

    completed_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title