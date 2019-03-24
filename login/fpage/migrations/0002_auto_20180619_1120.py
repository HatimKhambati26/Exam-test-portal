# Generated by Django 2.0.6 on 2018-06-19 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]