# Generated by Django 3.0 on 2020-02-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runoApp', '0009_auto_20200130_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunoRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=64)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runoApp.RunoDB')),
            ],
        ),
    ]
