# Generated by Django 3.2.7 on 2021-09-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mc',
            name='mcdisplay',
            field=models.BooleanField(default=True, verbose_name='홈페이지노출여부'),
        ),
        migrations.AddField(
            model_name='mc',
            name='mcmain',
            field=models.BooleanField(default=False, verbose_name='메인사회자'),
        ),
    ]
