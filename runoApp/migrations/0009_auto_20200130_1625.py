# Generated by Django 3.0 on 2020-01-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runoApp', '0008_kaveri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elokuva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='kaveri',
            name='elokuvat',
            field=models.ManyToManyField(to='runoApp.Elokuva'),
        ),
    ]