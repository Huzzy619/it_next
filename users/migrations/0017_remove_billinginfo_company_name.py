# Generated by Django 4.0.3 on 2022-05-30 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_billinginfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billinginfo',
            name='company_name',
        ),
    ]
