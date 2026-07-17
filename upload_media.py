import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from pathlib import Path
from django.core.files import File
from website.models import Project, Service


def upload_images():
    media_path = Path("media")

    # Upload Projects
    for project in Project.objects.all():
        if project.image:
            file_path = media_path / str(project.image)

            if file_path.exists():
                print(f"Uploading {file_path}")

                with open(file_path, "rb") as f:
                    project.image.save(
                        file_path.name,
                        File(f),
                        save=True
                    )

                print(f"Uploaded {project.title}")


    # Upload Services
    for service in Service.objects.all():
        if service.image:
            file_path = media_path / str(service.image)

            if file_path.exists():
                print(f"Uploading {file_path}")

                with open(file_path, "rb") as f:
                    service.image.save(
                        file_path.name,
                        File(f),
                        save=True
                    )

                print(f"Uploaded {service.name}")


if __name__ == "__main__":
    upload_images()