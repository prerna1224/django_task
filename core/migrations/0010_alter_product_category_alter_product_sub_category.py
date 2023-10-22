# Generated by Django 4.2.6 on 2023-10-21 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_product_category_alter_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.sub_category'),
        ),
    ]
