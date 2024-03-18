# Generated by Django 4.2.4 on 2023-12-08 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_family_img_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='title',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='plant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='plant.plant'),
        ),
    ]
