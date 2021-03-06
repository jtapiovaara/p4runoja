# Generated by Django 3.0 on 2020-01-30 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runoApp', '0004_runodb_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valokuva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(blank=True, max_length=64)),
                ('poempicture', models.ManyToManyField(to='runoApp.RunoDB')),
            ],
        ),
        migrations.CreateModel(
            name='Kirjoittaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.CharField(blank=True, max_length=3)),
                ('runodb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runoApp.RunoDB')),
            ],
        ),
    ]
