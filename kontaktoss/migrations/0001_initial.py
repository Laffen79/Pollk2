# Generated by Django 4.2 on 2023-05-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KontaktMelding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=100)),
                ('epost', models.EmailField(max_length=254)),
                ('melding', models.TextField()),
            ],
        ),
    ]
