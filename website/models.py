from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to="services/",
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
    
    from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="gallery/")
    category = models.CharField(max_length=50)
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title