# Generated by Django 4.2.5 on 2023-10-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_alter_blogs_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
