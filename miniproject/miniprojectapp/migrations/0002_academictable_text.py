# Generated by Django 4.2.5 on 2023-11-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academictable',
            name='text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
