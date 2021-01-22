# Generated by Django 3.1.2 on 2021-01-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('ap_Id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ap_name', models.CharField(max_length=200, null=True)),
                ('flat_count', models.IntegerField()),
                ('floor', models.IntegerField()),
            ],
        ),
    ]
