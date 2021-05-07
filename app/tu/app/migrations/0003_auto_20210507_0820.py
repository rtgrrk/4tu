# Generated by Django 3.2 on 2021-05-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='app.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('shipping', 'shipping'), ('shipped', 'shipped')], default='pending', max_length=255),
        ),
    ]
