# Generated by Django 4.1.7 on 2023-04-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_eco', '0003_alter_ecologiya_slug_alter_support_photo_forms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecologiya',
            name='slug',
            field=models.SlugField(max_length=16, unique=True, verbose_name='слаг'),
        ),
    ]
