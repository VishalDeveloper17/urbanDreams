# Generated by Django 3.1.2 on 2021-01-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UDAdminApp', '0005_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20, null=True)),
                ('s_charge', models.CharField(max_length=100000, null=True)),
            ],
        ),
    ]
