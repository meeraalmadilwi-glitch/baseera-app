from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Creates the baseera admin user if it does not exist'

    def handle(self, *args, **kwargs):
        email = 'bsseera.ai0@gmail.com'
        username = 'admin_baseera'
        password = 'AdminBaseera2026!'
        
        if not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user: {email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin user with email {email} or username {username} already exists.'))
