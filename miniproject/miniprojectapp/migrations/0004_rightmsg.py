# Generated by Django 4.2.7 on 2023-11-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniprojectapp', '0003_remove_academictable_text_academictable_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='rightmsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
    ]
