# Generated by Django 4.2 on 2023-04-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenFuelsNodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10)),
                ('postcity', models.CharField(max_length=255)),
                ('geo_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('geo_lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('inventory', models.TextField(blank=True)),
            ],
        ),
    ]