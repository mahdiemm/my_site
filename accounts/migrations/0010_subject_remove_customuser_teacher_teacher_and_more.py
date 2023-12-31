# Generated by Django 4.2.5 on 2023-11-13 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(default='#007bff', max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='teacher',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('userinfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('account', models.CharField(choices=[(1, 'teacher'), (2, 'organization')], max_length=100)),
                ('payment', models.CharField(choices=[(1, 'Zarin')], max_length=100)),
                ('identity', models.FileField(upload_to='')),
                ('documents', models.FileField(upload_to='')),
                ('body', models.TextField()),
                ('subject', models.ManyToManyField(related_name='subject', to='accounts.subject')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='Teacher',
            field=models.BooleanField(default=False),
        ),
    ]
