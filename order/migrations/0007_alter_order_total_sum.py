# Generated by Django 4.1.5 on 2023-01-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_sum',
            field=models.IntegerField(null=True),
        ),
    ]
