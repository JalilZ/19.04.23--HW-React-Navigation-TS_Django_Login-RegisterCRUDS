# Generated by Django 4.2 on 2023-04-17 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.CharField(default='placeholder.png', max_length=50),
        ),
    ]
