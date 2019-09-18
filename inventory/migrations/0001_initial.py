# Generated by Django 2.2.1 on 2019-09-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Items Ready to be Purchase'), ('SOLD', 'Items Sold Out'), ('Restocking', 'Re stocking in few days')], default='sold', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Items Ready to be Purchase'), ('SOLD', 'Items Sold Out'), ('Restocking', 'Re stocking in few days')], default='sold', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Items Ready to be Purchase'), ('SOLD', 'Items Sold Out'), ('Restocking', 'Re stocking in few days')], default='sold', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
