# Generated by Django 4.2.21 on 2025-05-10 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.CharField(max_length=45)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='inventoryapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.CharField(max_length=45)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availableQuantity', models.IntegerField()),
                ('productPrice', models.FloatField()),
                ('totalPrice', models.FloatField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='inventoryapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='OutgoingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityToOrder', models.IntegerField()),
                ('totalPriceBeforeDiscount', models.FloatField()),
                ('discount', models.FloatField()),
                ('totalPriceAfterDiscount', models.FloatField()),
                ('OrderDate', models.DateField(auto_now_add=True)),
                ('customerId', models.ManyToManyField(to='inventoryapp.supplier')),
                ('productId', models.ManyToManyField(to='inventoryapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='IncomingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availableQuantity', models.IntegerField()),
                ('productPrice', models.FloatField()),
                ('totalPrice', models.FloatField()),
                ('supplyDate', models.DateField(auto_now_add=True)),
                ('productId', models.ManyToManyField(related_name='incomingorder', to='inventoryapp.product')),
                ('supplierId', models.ManyToManyField(related_name='incomingorder', to='inventoryapp.supplier')),
            ],
        ),
    ]
