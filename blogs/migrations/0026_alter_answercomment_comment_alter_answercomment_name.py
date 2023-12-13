# Generated by Django 4.2.5 on 2023-11-09 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0025_answercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answercomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AnswerComments', to='blogs.comment'),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAnswerComments', to=settings.AUTH_USER_MODEL),
        ),
    ]