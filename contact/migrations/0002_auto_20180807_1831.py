# Generated by Django 2.1 on 2018-08-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('currentPos', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('languageProficient', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ProgrammingLang',
        ),
    ]
