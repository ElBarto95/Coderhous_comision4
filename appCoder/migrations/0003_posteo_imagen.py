# Generated by Django 4.1.2 on 2023-04-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCoder', '0002_posteo_delete_entregable'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]