# Generated by Django 4.1.7 on 2023-05-08 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_cartitem_book_alter_transaction_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
    ]
