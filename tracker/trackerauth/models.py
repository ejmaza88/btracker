import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Managers
class ArchiveModelVisibleManager(models.Manager):
    def get_queryset(self):
        return super(ArchiveModelVisibleManager, self).get_queryset().filter(archived=False)


class ArchiveModelHiddenManager(models.Manager):
    def get_queryset(self):
        return super(ArchiveModelHiddenManager, self).get_queryset().filter(archived=True)


# Main Models
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_app_admin = models.BooleanField(default=False)

    def __str__(self):
        """Return a human-readable string representing a User record"""
        return self.get_full_name()

    class Meta:
        ordering = ["first_name"]


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ArchiveModel(UUIDModel):
    """
    For models that will never be deleted, use an archive flag to hide them from normal operations.
    """

    archived = models.BooleanField(default=False)

    # Manager objs
    objects = ArchiveModelVisibleManager()
    archived_objs = ArchiveModelHiddenManager()
    all_objs = models.Manager()

    class Meta:
        abstract = True
