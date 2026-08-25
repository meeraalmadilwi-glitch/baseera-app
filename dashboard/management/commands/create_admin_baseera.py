from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import Profile

class Command(BaseCommand):
    help = 'Creates or updates the primary admin user with credentials'

    def handle(self, *args, **kwargs):
        # 1. Create or update primary admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@baseera.om',
                'first_name': 'مدير',
                'last_name': 'النظام',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        admin_user.set_password('admin123456')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.is_active = True
        admin_user.save()
        
        Profile.objects.get_or_create(
            user=admin_user,
            defaults={
                'company_name': 'منصة بصيرة للذكاء الاصطناعي',
                'project_type': 'other',
                'is_subscribed': True,
                'subscription_plan': 'enterprise',
            }
        )
        self.stdout.write(self.style.SUCCESS('Admin user "admin" is active with password "admin123456".'))

        # 2. Also ensure Mira21 has full superadmin privileges if present
        mira = User.objects.filter(username='Mira21').first()
        if mira:
            mira.is_staff = True
            mira.is_superuser = True
            mira.is_active = True
            mira.save()
            self.stdout.write(self.style.SUCCESS('User "Mira21" is configured with superadmin privileges.'))

