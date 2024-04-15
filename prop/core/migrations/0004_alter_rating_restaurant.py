# Generated by Django 5.0.4 on 2024-04-15 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='core.restaurant'),
        ),
    ]