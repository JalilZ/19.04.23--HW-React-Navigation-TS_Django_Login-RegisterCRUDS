# Generated by Django 4.2 on 2023-04-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='dairy', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='Random desc', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod',
            field=models.CharField(default='Random desc', max_length=50),
        ),
    ]
