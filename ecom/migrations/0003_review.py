# Generated by Django 5.0 on 2023-12-17 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('pros', models.CharField(blank=True, default='', max_length=522)),
                ('corns', models.CharField(blank=True, default='', max_length=522)),
                ('review', models.CharField(blank=True, default='', max_length=522)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.products')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
