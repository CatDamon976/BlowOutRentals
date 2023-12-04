# Generated by Django 4.2.5 on 2023-12-04 03:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(5)])),
                ('phone', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('abbrev', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.orders')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepages.states'),
        ),
    ]
