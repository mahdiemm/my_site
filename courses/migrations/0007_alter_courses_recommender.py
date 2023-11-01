# Generated by Django 4.2.5 on 2023-10-25 15:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_alter_courses_recommender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='recommender',
            field=models.ManyToManyField(blank=True, default=None, related_name='recommender_course', to=settings.AUTH_USER_MODEL),
        ),
    ]
