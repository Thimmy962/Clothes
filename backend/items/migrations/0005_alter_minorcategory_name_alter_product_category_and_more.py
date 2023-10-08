# Generated by Django 4.2.5 on 2023-10-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minorcategory',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='categoryItem', to='items.minorcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
