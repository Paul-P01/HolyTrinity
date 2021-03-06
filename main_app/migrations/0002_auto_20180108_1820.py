# Generated by Django 2.0.1 on 2018-01-08 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='church',
            options={'verbose_name_plural': 'Churches'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterField(
            model_name='person',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='church', to='main_app.Church'),
        ),
    ]
