# Generated by Django 4.0.4 on 2022-06-14 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartrige',
            name='model_series',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.printermodelseries'),
        ),
        migrations.AlterField(
            model_name='printerproducer',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]