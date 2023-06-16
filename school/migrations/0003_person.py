# Generated by Django 4.2.2 on 2023-06-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_newuser_reg_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]
