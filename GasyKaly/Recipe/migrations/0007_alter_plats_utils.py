# Generated by Django 5.1 on 2024-08-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0006_remove_plats_isrecent_remove_plats_isrecomanded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plats',
            name='utils',
            field=models.ManyToManyField(related_name='utils', to='Recipe.utils'),
        ),
    ]
