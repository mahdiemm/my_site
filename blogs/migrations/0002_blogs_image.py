# Generated by Django 4.2.5 on 2023-10-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, default='969.jpg', upload_to=''),
        ),
    ]
