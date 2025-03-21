# Generated by Django 5.0.3 on 2024-07-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_order_shipping_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20, verbose_name="The order's status"),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
