# website/management/commands/set_admin_password.py

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Sets the password for the superuser defined in environment variables.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write(self.style.ERROR('Superuser credentials not set in environment. Skipping.'))
            return

        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Password for superuser "{username}" has been set/reset successfully.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Superuser "{username}" does not exist. Please run create_superuser_on_deploy first.'))