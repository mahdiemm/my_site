# Generated by Django 4.2.5 on 2023-11-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_subject_remove_customuser_teacher_teacher_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='Teacher',
            new_name='is_teacher',
        ),
    ]