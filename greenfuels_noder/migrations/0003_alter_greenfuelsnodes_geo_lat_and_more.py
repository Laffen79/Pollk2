# Generated by Django 4.2 on 2023-04-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenfuels_noder', '0002_alter_greenfuelsnodes_geo_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenfuelsnodes',
            name='geo_lat',
            field=models.DecimalField(decimal_places=16, max_digits=18),
        ),
        migrations.AlterField(
            model_name='greenfuelsnodes',
            name='geo_lng',
            field=models.DecimalField(decimal_places=16, max_digits=18),
        ),
    ]
