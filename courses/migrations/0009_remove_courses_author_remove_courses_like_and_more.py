# Generated by Django 4.2.5 on 2023-11-05 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_courses_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='author',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='like',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='recommender',
        ),
    ]
