# Generated by Django 3.2.5 on 2023-04-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_auto_20230428_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Start', models.DateField()),
                ('End', models.DateField()),
                ('Description', models.TextField()),
                ('Resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
    ]
