# Generated by Django 4.2 on 2023-05-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer_automater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendanornode',
            name='address2',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]