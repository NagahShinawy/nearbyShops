# Generated by Django 3.1.4 on 2020-12-27 08:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
