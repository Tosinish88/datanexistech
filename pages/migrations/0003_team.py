# Generated by Django 5.0.4 on 2024-05-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_service_icon_service_icon2_alter_servicetitle_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('barcode', models.ImageField(blank=True, null=True, upload_to='barcode')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]