# Generated by Django 4.2.7 on 2023-12-11 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(choices=[('driver', 'driver'), ('sponsor', 'sponsor'), ('admin', 'admin')], default='driver', max_length=7)),
                ('mySponsor', models.CharField(choices=[('driver', 'driver'), ('sponsor', 'sponsor'), ('admin', 'admin')], default='NONE', max_length=7)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userRole', models.CharField(max_length=7)),
            ],
        ),
    ]
