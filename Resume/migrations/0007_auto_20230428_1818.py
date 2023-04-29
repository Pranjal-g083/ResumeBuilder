# Generated by Django 3.2.5 on 2023-04-28 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0006_skill_skillcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='KeyCoursesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Resume', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='KeyCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resume.keycoursescategory')),
            ],
        ),
    ]
