from django.contrib import admin
from .models import Service, Project
from .models import Gallery


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "created_at",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "location",
        "completed_date",
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "completed_date",
    )
    list_filter = ("category",)
    search_fields = ("title", "description")