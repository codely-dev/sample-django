# Generated by Django 3.1.6 on 2021-04-22 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('startdate', models.DateTimeField(verbose_name='Start')),
                ('enddate', models.DateTimeField(verbose_name='Ende')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
                ('submitted', models.DateField(auto_now_add=True, verbose_name='Erstelldatum')),
                ('category', models.IntegerField(choices=[(1, 'Höhenflug'), (2, 'Übungshang'), (3, 'Theorie'), (4, 'Reisen'), (5, 'SIKU/NSW'), (6, 'Sonstiges')], verbose_name='Icon')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.location')),
                ('organisator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Organisator', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='Teilnehmer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Kommentar')),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name='Erstelldatum')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
