# Generated by Django 2.0.1 on 2018-01-12 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='main_app.Role'),
        ),
    ]
