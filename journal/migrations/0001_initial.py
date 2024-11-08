# Generated by Django 5.1.3 on 2024-11-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_loss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('strategy', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]