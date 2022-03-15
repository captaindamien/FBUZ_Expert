# Generated by Django 4.0.1 on 2022-01-24 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expert', '0002_expertises_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertises',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
