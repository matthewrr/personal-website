# Generated by Django 2.0.2 on 2018-06-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180623_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(default='', upload_to='index/files/resume/'),
            preserve_default=False,
        ),
    ]
