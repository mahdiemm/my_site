# Generated by Django 4.2.5 on 2023-10-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_lessons_questions_delete_courseinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ('-created',)},
        ),
    ]
