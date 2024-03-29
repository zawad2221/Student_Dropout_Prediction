# Generated by Django 3.1.7 on 2021-03-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('nationaity', models.CharField(max_length=50)),
                ('place_of_birth', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('batch', models.IntegerField()),
                ('semester', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=255)),
                ('last_semester_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('question_asked_in_classroom', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')])),
                ('go_through_course_material', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')])),
                ('meet_with_academic_adviser', models.IntegerField()),
                ('group_study_hours', models.IntegerField()),
                ('absense_day', models.IntegerField()),
                ('parents_satisfaction', models.BooleanField()),
                ('education_status_of_parents', models.IntegerField(choices=[(0, 'SSC'), (1, 'HSC'), (2, 'Above HSC')])),
                ('s_class', models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')])),
            ],
        ),
    ]
