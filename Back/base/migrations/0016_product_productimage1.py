# Generated by Django 4.2 on 2023-04-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_product_category_alter_product_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage1',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]