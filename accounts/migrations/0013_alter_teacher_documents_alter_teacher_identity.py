# Generated by Django 4.2.5 on 2023-11-13 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_teacher_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='documents',
            field=models.FileField(upload_to='course_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='identity',
            field=models.FileField(upload_to='course_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])]),
        ),
    ]
