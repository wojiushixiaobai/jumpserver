# Generated by Django 2.2.13 on 2020-10-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0008_auto_20200819_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Comment'),
        ),
    ]
