# Generated by Django 4.2.4 on 2023-09-10 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0043_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewandrating',
            name='allo',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SMSApp.allocatedorder'),
        ),
    ]
