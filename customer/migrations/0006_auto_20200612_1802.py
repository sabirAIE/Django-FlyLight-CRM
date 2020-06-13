# Generated by Django 3.0.4 on 2020-06-12 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200612_0602'),
        ('customer', '0005_auto_20200612_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.adminUsers'),
        ),
    ]
