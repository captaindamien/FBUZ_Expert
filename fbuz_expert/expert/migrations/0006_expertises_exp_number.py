# Generated by Django 4.0.1 on 2022-03-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0005_expertises_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertises',
            name='exp_number',
            field=models.PositiveIntegerField(default=0, verbose_name='номер экспертизы'),
        ),
    ]
