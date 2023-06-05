# Generated by Django 4.2.1 on 2023-06-05 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='flights.flight'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ManyToManyField(related_name='reservation', to='flights.passenger'),
        ),
    ]
