# Generated by Django 3.2.7 on 2021-09-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HTSW', '0003_routes_r_count_stowaways'),
    ]

    operations = [
        migrations.AddField(
            model_name='routes',
            name='r_region',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
