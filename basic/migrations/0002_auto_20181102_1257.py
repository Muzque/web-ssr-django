# Generated by Django 2.1.2 on 2018-11-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.ImageField(default=None, upload_to='user_img'),
        ),
    ]