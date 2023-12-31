# Generated by Django 4.2.5 on 2023-11-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0002_academictable_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academictable',
            name='text',
        ),
        migrations.AddField(
            model_name='academictable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='culturaltable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventstable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nsstable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placementstable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportstable',
            name='type',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
