# Generated by Django 4.2.6 on 2023-10-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_id_alter_sub_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/pimg')),
                ('name', models.CharField(max_length=200)),
                ('price', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
