# Generated by Django 3.1.1 on 2020-09-17 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baby_name', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('profile_image', models.CharField(max_length=200)),
                ('birth_height', models.FloatField()),
                ('birth_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BabyMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('measure_date', models.DateField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babies.baby')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_measurements', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='modified_measurements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
