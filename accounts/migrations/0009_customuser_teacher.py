# Generated by Django 4.2.5 on 2023-11-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]
