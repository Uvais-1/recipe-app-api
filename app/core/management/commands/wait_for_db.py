"""
DJANGO Command to wait for databae to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django cmd to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for Command"""
        self.stdout.write('Waiting for database..')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Databases unavailable,waiting for a second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Databadse available! '))
