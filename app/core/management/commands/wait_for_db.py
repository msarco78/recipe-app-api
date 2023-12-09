"""
Django command to wait fot the database to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command on wait for database."""

    def handle(self, *args, **options):
        pass