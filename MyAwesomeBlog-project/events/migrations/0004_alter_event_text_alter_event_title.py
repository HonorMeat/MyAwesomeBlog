# Generated by Django 4.0.2 on 2022-02-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_изображение события_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Text',
            field=models.CharField(default='Text', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='Title',
            field=models.CharField(default='Title', max_length=300),
        ),
    ]