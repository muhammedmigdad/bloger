# Generated by Django 5.0.6 on 2024-07-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='short_descrption',
            new_name='short_description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='descrption',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
