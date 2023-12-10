from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mysprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamNum', models.IntegerField()),
                ('versNum', models.CharField(max_length=250)),
                ('releaseDate', models.CharField(max_length=250)),
                ('prodDesc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=250, verbose_name='first name')),
                ('lastName', models.CharField(max_length=250, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('username', models.CharField(max_length=250, verbose_name='username')),
                ('password', models.CharField(max_length=250, verbose_name='password')),
                ('role', models.CharField(help_text='D(driver) S(sponsor) A(admin)', max_length=1, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ID', models.IntegerField(primary_key=True, serialize=False)),

            ],
        ),
    ]
