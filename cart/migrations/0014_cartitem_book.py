# Generated by Django 4.1.7 on 2023-05-08 09:55

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_status'),
        ('cart', '0013_remove_cartitem_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo'),
            preserve_default=False,
        ),
    ]
