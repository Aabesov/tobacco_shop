# Generated by Django 4.1.5 on 2023-01-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]