# Generated by Django 4.1.1 on 2022-09-27 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0004_rename_quote_bet_odd'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
