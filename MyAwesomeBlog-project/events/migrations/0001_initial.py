# Generated by Django 4.0.2 on 2022-02-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.ImageField(upload_to='event_images/')),
                ('t', models.CharField(max_length=300)),
            ],
        ),
    ]
