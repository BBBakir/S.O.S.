# Generated by Django 4.2.2 on 2023-06-26 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_logisticscompany_has_district_costofoutsource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='RequestID',
        ),
    ]