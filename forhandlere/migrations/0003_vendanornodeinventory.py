# Generated by Django 4.2 on 2023-04-30 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forhandlere', '0002_vendanornodes_serialno'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendanorNodeInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='forhandlere.vendanornodes')),
            ],
        ),
    ]
