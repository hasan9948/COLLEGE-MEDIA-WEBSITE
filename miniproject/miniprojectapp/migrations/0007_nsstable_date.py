# Generated by Django 4.2.7 on 2023-11-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0006_eventstable_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='nsstable',
            name='date',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]