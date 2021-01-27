# Generated by Django 3.1.2 on 2021-01-27 14:39

from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    dependencies = [
        ('UDAdminApp', '0004_flats_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('paid', 'paid'), ('un-paid', 'un-paid')], max_length=20, null=True)),
                ('month', month.models.MonthField(help_text='some help...', verbose_name='Month Value')),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UDAdminApp.flats')),
            ],
        ),
    ]
