# Generated by Django 3.1.7 on 2021-03-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mobileno', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=200)),
                ('add', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
    ]