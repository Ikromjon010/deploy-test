# Generated by Django 4.0 on 2024-04-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('soni', models.IntegerField()),
                ('narxi', models.IntegerField()),
                ('muddat', models.DateField()),
                ('firma', models.CharField(max_length=200)),
            ],
        ),
    ]
