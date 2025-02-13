# Generated by Django 4.1.7 on 2023-04-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('avatar', models.ImageField(upload_to='')),
                ('mail', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.IntegerField()),
                ('create_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.account')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='book.bookinfo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.user')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.book')),
            ],
        ),
    ]
