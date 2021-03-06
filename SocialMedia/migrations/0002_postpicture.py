# Generated by Django 2.1.4 on 2019-03-28 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialMedia.Post')),
            ],
        ),
    ]
