# Generated by Django 4.1.2 on 2022-11-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product_users_wishlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active2",
            field=models.BooleanField(default=True),
        ),
    ]
