# Generated by Django 5.1 on 2024-08-20 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0007_alter_plats_utils'),
    ]

    operations = [
        migrations.AddField(
            model_name='plats',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('plat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to='Recipe.plats')),
            ],
        ),
    ]
