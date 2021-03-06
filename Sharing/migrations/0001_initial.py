# Generated by Django 2.1.4 on 2019-03-26 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField(default=1)),
                ('source_location', models.CharField(choices=[('lhr', 'Lahore'), ('fsd', 'Faisalabad'), ('isb', 'Islamabad')], max_length=15)),
                ('dest_location', models.CharField(choices=[('lhr', 'Lahore'), ('fsd', 'Faisalabad'), ('isb', 'Islamabad')], max_length=15)),
                ('car_model', models.CharField(max_length=20)),
                ('car_number', models.CharField(max_length=15)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarSharingAcceptance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('accepted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('carsharing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sharing.CarSharing')),
            ],
        ),
        migrations.CreateModel(
            name='LuggageSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField(default=1)),
                ('source_location', models.CharField(choices=[('lhr', 'Lahore'), ('fsd', 'Faisalabad'), ('isb', 'Islamabad')], max_length=15)),
                ('dest_location', models.CharField(choices=[('lhr', 'Lahore'), ('fsd', 'Faisalabad'), ('isb', 'Islamabad')], max_length=15)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
