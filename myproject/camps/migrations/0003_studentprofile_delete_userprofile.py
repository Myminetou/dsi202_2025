# Generated by Django 4.2 on 2025-05-10 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camps', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(blank=True, choices=[('M1', 'มัธยมศึกษาปีที่ 1'), ('M2', 'มัธยมศึกษาปีที่ 2'), ('M3', 'มัธยมศึกษาปีที่ 3'), ('M4', 'มัธยมศึกษาปีที่ 4'), ('M5', 'มัธยมศึกษาปีที่ 5'), ('M6', 'มัธยมศึกษาปีที่ 6'), ('VOCATIONAL', 'อาชีวศึกษา'), ('UNIVERSITY', 'มหาวิทยาลัย'), ('OTHER', 'อื่น ๆ')], max_length=20)),
                ('hobbies', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
